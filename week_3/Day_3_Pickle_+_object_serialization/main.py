from patient import Patient
from patient_service import PatientService
from patient_pickle_repository import PatientPickleRepository

repo = PatientPickleRepository("patient.pkl")
service = PatientService(repo)

new_patient1 = Patient(1, "John Doe", 30)
# new_patient2 = Patient(2, "Jane Smith", -5)  #  This should raise a ValueError

service.reg_patient(new_patient1)
# service.reg_patient(new_patient2)  # This line will not be executed due to the exception

for p in service.list_all():
    print(f"ID: {p.patient_id}, Name: {p.name}, Age: {p.age}")