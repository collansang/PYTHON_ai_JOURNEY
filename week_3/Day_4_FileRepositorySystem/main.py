from services.patientservices import PatientService
from repositories.patient_JSON_repository import PatientJSONRepository  
from repositories.patient_memory_repository import InMemoryPatientRepository
from models.patient import Patient  

repo = PatientJSONRepository("patients.json")

service = PatientService(repo)

service.register_patient(Patient("P1", "John", 30))
service.register_patient(Patient("P2", "Alice", 25))

patients = service.list_patients()
for patient in patients:
    print(f"ID: {patient.pid}, Name: {patient.name}, Age: {patient.age}")

