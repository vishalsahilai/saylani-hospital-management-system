from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.staff import StaffCreate, StaffUpdate, StaffResponse
from app.crud.staff import create_staff, get_staff, get_all_staff, update_staff, delete_staff