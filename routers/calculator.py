from fastapi import APIRouter, HTTPException
from calculator.calc import calculate

router = APIRouter()


@router.get("/calculate")
def calculate_numbers(a, b: float, choice: str):
    result = calculate(a, b, choice)
    if result is None:
        raise HTTPException(status_code=400, detail="Invalid choice")
    return {"result": result}
