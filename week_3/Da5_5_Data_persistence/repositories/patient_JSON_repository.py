import os
import json
from repositories.patient_repository import PatientRepository
from models.patient import Patient

class PatientJSONRepository(PatientRepository):
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w") as file:
                json.dump([], file)
        
    def _load(self):
        with open(self.file_path, "r") as file:
            return  json.load(file)
    
    def _save(self, data):
        with open (self.file_path, "w") as file:
            json.dump(data, file, indent = 4)
            
    def add(self, patient):
        data = self._load()
        data.append(patient.to_dict())
        self._save(data)
        
    def get_by_id(self,pid):
        data = self._load()
        for i in data:
            if i["pid"] == pid:
                return Patient.from_dict(i)
        return None
    
    def list_all(self):
        return [Patient.from_dict(p) for p in self._load()]
        
        
            
        