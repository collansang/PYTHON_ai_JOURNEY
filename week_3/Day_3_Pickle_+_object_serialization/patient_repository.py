from abc import ABC, abstractmethod
class PatientRepository(ABC):
    @abstractmethod
    #save the patient object to the repository
    def save(self, patient):
        pass
    
    @abstractmethod
    #retrieve the patients
    def list_all(self):
        pass
    