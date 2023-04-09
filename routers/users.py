from fastapi import APIRouter, Depends
from database import sessionLocal
from sqlalchemy.orm import Session
import models

router = APIRouter(
    prefix="/users",
    tags=["users"],
    responses={401: {"user": "Not authorized"}}
)


def get_db():
    try: 
        db = sessionLocal()
        yield db
    finally:
        db.close()

@router.get("/")
async def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.Users).all()