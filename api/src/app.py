from datetime import date
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
#from pydantic import BaseModel, create_model
#from typing import Optional
from sqlmodel import Field, SQLModel, create_engine, Session
from models import User, UserAuth
from routes import user, auth

app = FastAPI()
# TODO: LOOK MORE INTO THESE LATER
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(auth.router, prefix="/auth")
app.include_router(user.router, prefix="/user")

