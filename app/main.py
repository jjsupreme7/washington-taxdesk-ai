from fastapi import FastAPI
from chatbot2 import router as chatbot_router

app = FastAPI()

# Root test route
@app.get("/")
def read_root():
    return {"message": "Washington Tax Desk AI is running."}

# Mount your chatbot endpoints
app.include_router(chatbot_router)

