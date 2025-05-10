from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, Base, get_db
from models.users import User
from schemas.userSchema import UserCreate
from routes import userRoutes

# Create all tables
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(userRoutes.router)
@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI app!"}

