#rules in the clinic

class PatientService:
    def __init__(self, repository):
        self.repository = repository#dependency injection
        
    def reg_patient(self, patient):
        if patient.age<0:
            raise ValueError("Age cannot be a negative value")
         
        self.repository.save(patient)#delegate storage
        
    def list_all(self):
        return self.repository.list_all()#delegate retrieval