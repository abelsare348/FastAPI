from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db  # Import your database dependency
from schemas.userSchema import UserCreate#, UserResponse  # Import Pydantic schemas
from cruds.userCrud import create_user, get_user, get_users, update_user, delete_user  # Import CRUD functions
from models.users import User 

router = APIRouter()

# Create a new user
@router.post("/create_user", response_model=UserCreate)
def create_user_route(user: UserCreate, db: Session = Depends(get_db)):
    """Create a new user."""
    create_user(db=db, user=user)
    return user

# Get a user by ID
@router.get("/get_user/{user_id}", response_model=UserCreate)
def read_user(user_id: int, db: Session = Depends(get_db)):
    """Retrieve a user by their ID."""
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Get a list of users with pagination
@router.get("/user_list", response_model=list[UserCreate])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    """Retrieve a list of users with optional pagination."""
    users = get_users(db, skip=skip, limit=limit)
    return users

# Update a user by ID
@router.put("/update_user/{user_id}", response_model=UserCreate)
def update_user_route(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    """Update an existing user."""
    db_user = update_user(db, user_id=user_id, name=user.name, age=user.age)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

# Delete a user by ID
@router.delete("/delete_user/{user_id}", response_model=UserCreate)
def delete_user_route(user_id: int, db: Session = Depends(get_db)):
    """Delete a user by their ID."""
    db_user = delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
