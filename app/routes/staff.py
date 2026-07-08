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

@router.get("/{staff_id}", response_model=StaffResponse)
def fetch_staff(staff_id: int, db: Session = Depends(get_db)):
    staff = get_staff(db, staff_id)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return staff

@router.put("/{staff_id}", response_model=StaffResponse)
def edit_staff(staff_id: int, data: StaffUpdate, db: Session = Depends(get_db)):
    staff = update_staff(db, staff_id, data)
    if not staff:
        raise HTTPException(status_code=404, detail="Staff not found")
    return staff