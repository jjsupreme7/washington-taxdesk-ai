from fastapi import FastAPI
from .chatbot2 import router as chatbot_router

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Washington Tax Desk AI is running."}

app.include_router(chatbot_router)



