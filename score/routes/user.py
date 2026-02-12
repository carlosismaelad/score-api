from fastapi import APIRouter
from sqlmodel import Session, select
from score.models.user import User, UserResponse, UserRequest
from score.db import ActiveSession
from typing import List

router = APIRouter()

@router.get("/")
async def list_users(*, session: Session = ActiveSession) -> List[UserResponse]:
  """List all users from database"""
  users = session.exec(select(User)).all()
  return users

@router.get("/{username}/")
async def get_user_by_username(*, session: Session = ActiveSession, username: str) -> UserResponse:
  """Get a user by username"""
  query = select(User).where(User.username == username)
  user = session.exec(query).first() # TODO: handle exceptions
  if not user:
    return {"error": "User not found"}
  return user

@router.post("/", status_code=201)
async def create_user(*, session: Session = ActiveSession, user: UserRequest) -> UserResponse:
  """Creates a nes user"""
  db_user = User.from_orm(user)
  session.add(db_user)
  session.commit() # TODO: handle exceptions
  session.refresh(db_user)
  return db_user