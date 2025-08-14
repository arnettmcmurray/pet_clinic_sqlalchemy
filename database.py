# === Engine Room ===
# This file handles the SQLAlchemy engine, session, and Base import

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///pet_clinic.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()