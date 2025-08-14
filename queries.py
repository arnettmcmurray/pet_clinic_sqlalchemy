# === Playbook for reading data ===
from database import Session
from models import Owner, Pet, Veterinarian, Appointment

session = Session()

# --- Show all pets owned by Arnett ---
arnett = session.query(Owner).filter_by(name="Arnett").first()
if arnett:
    print(f"Pets owned by {arnett.name}:")
    for pet in arnett.pets:
        print(f"- {pet.name} ({pet.species})")
else:
    print("Owner not found.")

# --- Show all appointments for Dr. Moodyblue ---
vet = session.query(Veterinarian).filter_by(name="Dr. Moodyblue").first()
if vet:
    print(f"\nAppointments for {vet.name}:")
    for appt in vet.appointments:
        print(f"- Pet: {appt.pet.name}, Date: {appt.time}, Reason: {appt.reason}")
else:
    print("Vet not found.")
