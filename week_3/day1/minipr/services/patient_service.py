from models.patient import Patient
from repositories.patient_repo import PatientRepository

class Patient_service:
    def __init__(self):
        self.repo = PatientRepository()
        
    def add_patient(self, name : str, age : int ):
        if not name.strip():
            raise ValueError("Name cannot be empty")
        if age < 0 or age >= 120:
            raise ValueError("Age must be betw 0 and 120")
        
        patients = self.repo.load_all()
        patients.append(Patient(name, age))
        self.repo.save_all(patients)
    def list_patients(self):
        return self.repo.load_all()