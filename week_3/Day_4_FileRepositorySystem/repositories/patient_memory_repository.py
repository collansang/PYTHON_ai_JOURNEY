from repositories.patient_repository import PatientRepository

class InMemoryPatientRepository(PatientRepository):
    def __init__(self,):
        self._data = {}
        
    def add(self, patient):
        self._data.append(patient)
        
    def get_all(self):
        return list(self.data)
    