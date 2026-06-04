from fastapi import APIRouter, HTTPException
from dotenv import load_dotenv
from generator_image.image_generator import generate_image
from openai import AsyncOpenAI
import os

load_dotenv()
router = APIRouter()
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))


@router.post("/generate_image")
async def generate_image_prompt(prompt: str):
    result = generate_image(prompt)
    return {"link for the image": result}
