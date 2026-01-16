from abc import ABC, abstractmethod

class PatientRepository(ABC):
    
    @abstractmethod
    def add(self, patient):
        pass
    
    @abstractmethod
    def save(self):
        pass