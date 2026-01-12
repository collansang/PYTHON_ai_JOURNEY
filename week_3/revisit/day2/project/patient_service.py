class PatientService:
    def __init__(self,repository):
        self.repository = repository
        
    def register_patient(self,patient):
        if patient.age < 0:
            raise ValueError("Age cannot be negative")
        self.repository.save(patient)
        
    def list_patients(self):
        return self.repository.list_all()
    
        