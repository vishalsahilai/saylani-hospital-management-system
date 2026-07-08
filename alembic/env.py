# Find this:
target_metadata = None

# Replace with:
from app.models import Doctor, Patient, Staff
from app.database import Base
from app.config import settings

target_metadata = Base.metadata