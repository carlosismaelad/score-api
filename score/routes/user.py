from fastapi import APIRouter
from sqlmodel import Session, select
from score.models.user import User, UserResponse
from score.db import ActiveSession
from typing import List

router = APIRouter()

@router.get("/")
async def list_users(*, session: Session = ActiveSession) -> List[UserResponse]:
  """List all users from database"""
  users = session.exec(select(User)).all()
  return users