
from abc import ABC, abstractmethod

class Record(ABC):
    @abstractmethod
    def save(self, data):
        pass

class Patient(Record):
    def save(self): 
        return {"name": "Alice"}# ❌ missing data parameter
        


patient = Patient()
print(patient.save())