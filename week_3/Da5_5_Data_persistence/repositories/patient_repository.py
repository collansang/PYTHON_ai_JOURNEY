from abc import ABC, abstractmethod

class PatientRepository(ABC):
    @abstractmethod
    def add(self, patient):
        pass
    def get_by_id(self, pid):
        pass
    @abstractmethod
    def list_all(self):
        pass
    

