from models import Owner, Pet, Vet, Appointment
from database import session

# Create owners
owner1 = Owner(name="Alice")
owner2 = Owner(name="Bob")

# Create pets
pet1 = Pet(name="Rex", species="Dog", owner=owner1)
pet2 = Pet(name="Whiskers", species="Cat", owner=owner2)

# Create vets
vet1 = Vet(name="Dr. Smith")
vet2 = Vet(name="Dr. Jones")

# Create appointments
appt1 = Appointment(reason="Checkup", pet=pet1, vets=[vet1])
appt2 = Appointment(reason="Vaccination", pet=pet2, vets=[vet1, vet2])

session.add_all([owner1, owner2, pet1, pet2, vet1, vet2, appt1, appt2])
session.commit()
