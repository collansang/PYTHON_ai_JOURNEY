from repositories.patient_memory_repository import PatientRepository
import json
from models.patient import Patient
class PatientJSONRepository(PatientRepository):
    def __init__(self, file_path):
        self.file_path = file_path
        
    def add(self, patient):
            patients = self.get_all()
            patients.append(patient)
            self.save(patients)
            
    def get_all(self):
        try:
            with open(self.file_path, "r")as file:
                data = json.load(file)
                return[Patient.from_dict(item) for item in data]
        except FileNotFoundError:
            return[]
        
    def save(self,patients):
            with open(self.file_path, "w") as file:
                json.dump([p.to_dict()for p in patients], file)
        