from models.patient import Patient
from repositories.memory_patient_repository import PatintRepository
from repositories.patient_JSON_repository import PatientJSONRepository
from services.patient_service import PatientService

repo = PatientJSONRepository("patients.json")
services = PatientService(repo)


patients  = {
    Patient(pid = 1, name = "Collan Tirop", age = 21, weight = 50, height= 1.2),
    Patient(pid = 2, name = "Kimtai Sang", age = 30, weight = 70, height= 1.8),
    Patient(pid = 3, name = "Alfred Nyongesa", age = 25, weight = 80, height= 1.75),
    Patient(pid = 4, name = "Silas Otieno", age = 28, weight = 65, height= 1.65)
    
}
for patient in patients:
    services.register_patient(patient)

patientss = services.list_patients()
for p in patientss:
    print(f"ID: {p.pid},Name: {p.name}, Age: {p.age}")