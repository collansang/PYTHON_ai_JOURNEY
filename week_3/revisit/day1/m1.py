import json
from abc import ABC, abstractmethod

class Patient:
    def __init__(self,patient_id, name, age ):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        
    def to_dict(self):
        return{
            "patient_id" : self.patient_id,
            "name" : self.name,
            "age" : self.age
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(#cls = clas Patient
                   #data = dictionary
            patient_id = data["patient_id"],
            name = data["name"],
            age = data["age"]
        )
patients = [
    Patient(1, "Collo", 21),
    Patient(2, "Moses", 22),
    Patient(3, "Enock", 23)
]
data = []
for patient in patients:
    data.append(Patient.to_dict(patient))
    
with open ("patients.json", "w") as file:
    json.dump(data, file, indent=4) #serializing to json file
    
with open("patients.json", "r") as file:
    data = json.load(file)
patients = []
for item in data:
    patients.append(Patient.from_dict(item)) #deserializing from json file to dictionary then to object
for p in patients:
    print(p.patient_id, p.name, p.age)


class PatientRepository(ABC):
    @abstractmethod
    def load_all(self):
        pass

    @abstractmethod
    def save_all(self, patients):
        pass
    
class PatientJSONRepository(PatientRepository):
    def __init__(self, filepath):
        self.file_path = filepath
    def load_all(self):
        try:
            with open(self.file_path, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return []
        patients = []
        for item in data:
            patients.append(Patient.from_dict(item))
        return patients

    def save_all(self, patients):
        data = [patient.to_dict() for patient in patients]
        with open(self.file_path, "w") as file:
            json.dump(data, file, indent=4)