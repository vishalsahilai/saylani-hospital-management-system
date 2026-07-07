from sqlalchemy.orm import Session
from app.models.staff import Staff
from app.schemas.staff import StaffCreate, StaffUpdate

def create_staff(db: Session, data: StaffCreate) -> Staff:
    staff = Staff(**data.model_dump())
    db.add(staff)
    db.commit()
    db.refresh(staff)
    return staff