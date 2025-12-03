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
    
    def name(self):
        return "age validator"
    
    def validate(self):
        return "age valid"
    pass


class TemperatureValidator(BaseValidator):
    def name(self):
        return "temp validation"
    
    def validate(self, Patient):
        if Patient.temperature > 37.5:
            return "fever"
        elif Patient.temperature < 35:
            return "hypothermia"
        else:
            return "normal"
   

class Patient:
    def __init__(self, name, age, temperature):
        self.name = name
        self.age = age
        self.temperature = temperature
        
        def __repr__(self):
            return f"Patient (name = {self.name},age = {self.age}), temperature = {self.temperature}"
      
      
def run_validation(patient, validators: list):
    for validator in validators:
        validate = validator.validate(patient)    
        if validate is True:
                print(f"{validator.name} OK")
        else:
            print(f"{validator.name} "+ validate)   