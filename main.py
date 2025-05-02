from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from routers import country
from routers import model
from dotenv import load_dotenv
import models
import os
from database import engine
from crud.country import init_country_data
from crud.model import init_model_data

load_dotenv()
VIEWER_URL = os.getenv("DATABASE_URL")
origins = [
    "http://localhost:5173",  
    "http://127.0.0.1:5173"
]

models.Base.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_country_data()
    init_model_data()
    yield

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    # allow_origins=[VIEWER_URL],  # Vite default port
    allow_origins=origins, 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





app.include_router(country.router) 
app.include_router(model.router)

