#simply the brain  that decides what should happen
        #enfoces rules
        #decide when storage should happen
        #coordinate actions

class PatientService:#responsible  for all patient-related actions and rules
    def __init__(self, repo):
        self.repo = repo#will help save the patient.
        
    def regiter_patient(self, patient):#someone wants to add patient to the system. is this actiopn allowed
        if patient.age <= 0:#patients age must make sense...
            raise ValueError("Invalid age")#otherwise raise an error
        self.repo.save(patient)#i approve this patient, repo you handle persistance
    def list_patients(self):#repo, give me all patients as objects
        return self.repo.get_all()
        
        
    