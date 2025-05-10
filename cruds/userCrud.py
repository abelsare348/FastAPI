from sqlalchemy.orm import Session
from models.users import User
from schemas.userSchema import UserCreate

def create_user(db: Session, user: UserCreate):
    # Create a new User instance
    db_user = User(name=user.name, age=user.age)
    # Add and commit the user to the database
    db.add(db_user)
    db.commit()
    db.refresh(db_user)  # Refresh to load the new data (like the assigned id)
    return db_user

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()

def update_user(db: Session, user_id: int, name: str = None, age: int = None):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        if name:
            db_user.name = name
        if age is not None:
            db_user.age = age
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user
