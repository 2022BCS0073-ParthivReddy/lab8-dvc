from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Housing Price Model API"}