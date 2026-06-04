from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MIN_PROMPT_LENGTH = 3
MAX_PROMPT_LENGTH = 500


def generate_image(prompt: str) -> str:
    """
    Generates an image using OpenAI and returns it as a base64 string.
    """

    if not isinstance(prompt, str):
        raise ValueError("Prompt must be a string")

    prompt = prompt.strip()

    if not prompt:
        raise ValueError("Prompt cannot be empty")

    if len(prompt) < MIN_PROMPT_LENGTH:
        raise ValueError(f"Prompt must contain at least {MIN_PROMPT_LENGTH} characters")

    if len(prompt) > MAX_PROMPT_LENGTH:
        raise ValueError(f"Prompt must contain at most {MAX_PROMPT_LENGTH} characters")

    result = client.images.generate(model="gpt-image-1-mini", prompt=prompt)

    return result.data[0].b64_json
