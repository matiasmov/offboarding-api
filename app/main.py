from fastapi import FastAPI
from dotenv import load_dotenv

from app.routers import offboarding 


load_dotenv()


app = FastAPI() 

app.include_router(offboarding.router, prefix="/api")

@app.get("/")
def home():
    return {"status": "Online"}