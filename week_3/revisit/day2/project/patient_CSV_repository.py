from abc import ABC, abstractmethod
import csv
from patient import Patient


class PatientRepository(ABC):
    @abstractmethod
    def save(self, patient):
        pass
    
    @abstractmethod
    def list_all(self):
        pass
    
    
    
class PatientCSVRepository(PatientRepository):
    def __init__(self, file_path):
        self.file_path = file_path
        
    def save(self, patient):
        with open(self.file_path, mode = "a", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=["patient_id", "name","age"])
            if file.tell() == 0:
                writer.writeheader()
            writer.writerow(patient.to_dict())
        
    def list_all(self):
        patients = []
        with open(self.file_path, mode = "r", newline= "")as file:
            reader = csv.DictReader(file)
            for row in reader:
                patients.append(Patient.from_dict(row))
        return patients
    