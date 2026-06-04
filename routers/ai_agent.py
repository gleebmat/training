import os
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from openai import AsyncOpenAI
from dotenv import load_dotenv

load_dotenv()
router = APIRouter()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
history: list[dict] = []

SYSTEM_PROMPT = {
    "role": "system",
    "content": (
        "You are a helpful, concise assistant. "
        "Answer clearly and accurately. "
        "If you don't know something, say so."
    ),
}


class AskRequest(BaseModel):
    question: str


class AskResponse(BaseModel):
    answer: str
    confidence: str = Field(default="high", description="Confidence level")


@router.post("/ask", response_model=AskResponse)
async def ask(request: AskRequest):
    history.append({"role": "user", "content": request.question})

    try:
        response = await client.chat.completions.parse(
            model="gpt-4o-mini",
            messages=[SYSTEM_PROMPT] + history,
            temperature=0.7,
            max_tokens=1024,
            response_format=AskResponse,
        )
    except Exception as e:
        history.pop()
        raise HTTPException(status_code=502, detail=f"OpenAI error: {str(e)}")

    parsed = response.choices[0].message.parsed
    history.append({"role": "assistant", "content": parsed.answer})
    return parsed


@router.get("/get_history")
def get_history():

    return {"history": history}


@router.delete("/clear_history")
def clear_history():
    history.clear()
    return {"detail": "History cleared."}
