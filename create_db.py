from sqlalchemy import create_engine
from base import Base

engine = create_engine("sqlite:///pet_clinic.db")

Base.metadata.create_all(engine)
print("Database created as pet_clinic.db")
