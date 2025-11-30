from abc import ABC, abstractmethod

class Record(ABC):
    @abstractmethod
    def to_dict(self):
        pass
    
    @abstractmethod
    def validate(self):
        pass
    
class Patient(Record): #class Patient must have methods to_dict and validate as in Record, otherwise it doent instanciate. To try it remove/comment out one method below and run it to see the error.
    def to_dict(self):
        return {"name" : "john"}
    
    def validate(self):
        return "ok"

patient = Patient()
print(patient.to_dict())
print(patient.validate())