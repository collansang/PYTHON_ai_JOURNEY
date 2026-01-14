from abc import ABC, abstractmethod

class PatientRepository(ABC):
    @abstractmethod
    def add(self, patient):
        """Add a new patient to the repository."""
        pass
    
    @abstractmethod
    def get_all(self, patient_id):
        """retrieve patient with their id"""
        pass
    