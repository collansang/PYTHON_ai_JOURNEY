class PatientService:
    def __init__(self, repository):
        self.repository = repository

    def register_patient(self, patient):
        if patient.age < 0:
            raise ValueError("Invalid age")

        self.repository.add(patient)

    def list_patients(self):
        return self.repository.get_all()
