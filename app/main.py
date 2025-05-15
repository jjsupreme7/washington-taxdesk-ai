from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Washington Tax Desk AI is running."}
