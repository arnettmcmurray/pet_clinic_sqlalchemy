# === The Models – This is the Chain ===
# All tables for the pet clinic: owners, pets, vets, appointments

from sqlalchemy import Column, Integer, String, ForeignKey, Table, DateTime
from sqlalchemy.orm import relationship, mapped_column
from database import Base

# === Junction table for many-to-many ===
vet_appointments = Table(
    "vet_appointments",
    Base.metadata,
    Column("vet_id", ForeignKey("veterinarians.id"), primary_key=True),
    Column("appointment_id", ForeignKey("appointments.id"), primary_key=True)
)

class Owner(Base):
    __tablename__ = "owners"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    email = mapped_column(String)

    # one-to-many: one owner has many pets
    pets = relationship("Pet", back_populates="owner")

class Pet(Base):
    __tablename__ = "pets"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    species = mapped_column(String)
    age = mapped_column(Integer)
    owner_id = mapped_column(ForeignKey("owners.id"))

    # link back to owner
    owner = relationship("Owner", back_populates="pets")
    # one-to-many: one pet can have many appointments
    appointments = relationship("Appointment", back_populates="pet")

class Veterinarian(Base):
    __tablename__ = "veterinarians"
    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String)
    specialty = mapped_column(String)

    # many-to-many via junction
    appointments = relationship("Appointment", secondary=vet_appointments, back_populates="veterinarians")

class Appointment(Base):
    __tablename__ = "appointments"
    id = mapped_column(Integer, primary_key=True)
    time = mapped_column(DateTime)
    reason = mapped_column(String)
    pet_id = mapped_column(ForeignKey("pets.id"))

    pet = relationship("Pet", back_populates="appointments")
    veterinarians = relationship("Veterinarian", secondary=vet_appointments, back_populates="appointments")