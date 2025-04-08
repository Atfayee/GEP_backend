from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine
from models.country import SQLModel
from routers import countries
from dotenv import load_dotenv
import os

load_dotenv()
VIEWER_URL = os.getenv("DATABASE_URL")

app = FastAPI()

# Allow React frontend to access the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=[VIEWER_URL],  # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SQLModel.metadata.create_all(engine)

   

app.include_router(countries.router) 