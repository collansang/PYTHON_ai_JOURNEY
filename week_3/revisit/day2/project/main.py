from patient import Patient
from patient_CSV_repository import PatientCSVRepository
from patient_service import PatientService

repo = PatientCSVRepository("patients.csv")
service = PatientService(repo)

p1 = Patient("001", "John Doe", 30)
p2 = Patient("002", "Jane Smith", 25)

service.register_patient(p1)
service.register_patient(p2)

for patient in service.list_patients():
    print(f"ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}")