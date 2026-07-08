from fastapi import FastAPI
from app.routes import doctor_router, patient_router, staff_router

app = FastAPI(
    title="Hospital Management System",
    description="API for managing doctors, patients and staff",
    version="1.0.0"
)

app.include_router(doctor_router)
app.include_router(patient_router)
app.include_router(staff_router)