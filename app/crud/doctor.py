from sqlalchemy.orm import Session
from app.models.doctor import Doctor
from app.schemas.doctor import DoctorCreate, DoctorUpdate

def create_doctor(db: Session, data: DoctorCreate) -> Doctor:
    doctor = Doctor(**data.model_dump())
    db.add(doctor)
    db.commit()
    db.refresh(doctor)
    return doctor

def get_doctor(db: Session, doctor_id: int) -> Doctor | None:
    return db.query(Doctor).filter(Doctor.id == doctor_id).first()

def get_all_doctors(db: Session) -> list[Doctor]:
    return db.query(Doctor).all()

def update_doctor(db: Session, doctor_id: int, data: DoctorUpdate) -> Doctor | None:
    doctor = get_doctor(db, doctor_id)
    if not doctor:
        return None
    for key, value in data.model_dump(exclude_unset=True).items():
        setattr(doctor, key, value)
    db.commit()
    db.refresh(doctor)
    return doctor

def delete_doctor(db: Session, doctor_id: int) -> bool:
    doctor = get_doctor(db, doctor_id)
    if not doctor:
        return False
    db.delete(doctor)
    db.commit()
    return True