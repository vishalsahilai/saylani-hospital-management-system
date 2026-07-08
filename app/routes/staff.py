from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.staff import StaffCreate, StaffUpdate, StaffResponse
from app.crud.staff import create_staff, get_staff, get_all_staff, update_staff, delete_staff

router = APIRouter(prefix="/staff", tags=["Staff"])


@router.post("/", response_model=StaffResponse)
def add_staff(data: StaffCreate, db: Session = Depends(get_db)):
    return create_staff(db, data)

@router.get("/", response_model=list[StaffResponse])
def list_staff(db: Session = Depends(get_db)):
    return get_all_staff(db)