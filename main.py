from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
# from routers import calculator, agent, images

load_dotenv()

app = FastAPI(
    title="First trainig project",
    description="Calculator, AI Agent, and Image Generation endpoints",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(calculator.router, prefix="/calculator", tags=["Calculator"])
# app.include_router(agent.router, prefix="/agent", tags=["AI Agent"])
# app.include_router(images.router, prefix="/images", tags=["Image Generation"])


@app.get("/", tags=["Health"])
def root():

    return {"status": "ok", "message": "The project is working!"}
