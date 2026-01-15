class PatientService:
    def __init__(self, repository):
        self.repository = repository
        
    def register_patient(self,patient):
        if self.repository.get_by_id(patient.pid):
            raise ValueError(f"Patient with ID {patient.pid} already exists.")
        self.repository.add(patient)
        
    def list_patients(self):
        return self.repository.list_all()
    