# === Load Me Up ===
# This file seeds your DB with some fake data

from datetime import datetime
from database import session, Base, engine
from models import Owner, Pet, Veterinarian, Appointment

Base.metadata.create_all(engine)

# Owners and pets
o1 = Owner(name="Arnett", email="arnett@example.com")
p1 = Pet(name="Bubba", species="Cat", age=7, owner=o1)
p2 = Pet(name="Obi", species="Dog", age=4, owner=o1)

# Vets
v1 = Veterinarian(name="Dr. Moodyblue", specialty="General")
v2 = Veterinarian(name="Dr. Currie", specialty="Surgery")

# Appointments
a1 = Appointment(time=datetime(2025, 8, 9, 14, 0), reason="Routine check-up", pet=p1)
a1.veterinarians.extend([v1])

a2 = Appointment(time=datetime(2025, 8, 10, 11, 0), reason="Limping issue", pet=p2)
a2.veterinarians.extend([v2])

session.add_all([o1, p1, p2, v1, v2, a1, a2])
session.commit()

print("DB seeded.")