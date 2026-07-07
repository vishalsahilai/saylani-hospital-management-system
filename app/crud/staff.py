from sqlalchemy.orm import Session
from app.models.staff import Staff
from app.schemas.staff import StaffCreate, StaffUpdate

def create_staff(db: Session, data: StaffCreate) -> Staff:
    staff = Staff(**data.model_dump())
    db.add(staff)
    db.commit()
    db.refresh(staff)
    return staff

def get_staff(db: Session, staff_id: int) -> Staff | None:
    return db.query(Staff).filter(Staff.id == staff_id).first()

def get_all_staff(db: Session) -> list[Staff]:
    return db.query(Staff).all()