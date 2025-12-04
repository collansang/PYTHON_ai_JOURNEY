from abc import ABC, abstractmethod

class BaseValidator(ABC):
    @property
    @abstractmethod
    def name(self):
        pass
    
    @abstractmethod
    def validate(self, patient):
        pass
    

class LoggingMixin():
    def log(self, message):
        print(f"LOG: {message}")
        
class AgeValidator(BaseValidator, LoggingMixin):
    @property
    def name(self):
        return "AgeValidator"
    
    def validate(self, patient):
        if patient.age  < 0 or patient.age >120:
            raise ValueError("age out of range. Should be btw 0 and 120")
        return True    

class TemperatureValidator(BaseValidator):
    @property
    def name(self):
        return "TemperatureValidator"
    
    def validate(self, patient):
        if not (34 <= patient.temperature <= 42):
            raise ValueError("temperature out of range. Should be btw 34 and 42")
        return True
           
           

class Patient:
    def __init__(self, name, age, temperature):
        self.name = name
        self.age = age
        self.temperature = temperature
        
    def __repr__(self):
        return f"Patient (name = {self.name},age = {self.age}), temperature = {self.temperature}"
def run_validations(patient, validators: list):
    for validator in validators:
      
            if isinstance(validator, LoggingMixin):
                validator.log(f"validating with {validator.name} ")
            try:    
                  validator.validate(patient)
                  print(f"{validator.name}  ok") 
            except ValueError as e:
                print(f"{validator.name} FAILED: {e}")
                
        
           


patient1 = Patient("Collan", 21, 37)
patient2 = Patient("John", 150, 39)
patient3 = Patient("Doe", 25, 50)
validators = [AgeValidator(), TemperatureValidator()]
run_validations(patient1, validators)
run_validations(patient2, validators)
run_validations(patient3, validators)
