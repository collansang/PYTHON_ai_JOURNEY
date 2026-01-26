class MedicationOrder:
    def __init__(self, base_dose_mg, dosing_policy):
        self.base_dose_mg = base_dose_mg
        self.dosing_policy = dosing_policy
        
    def administer(self,patient):
        final_dose = self.dosing_policy.calculate(self.base_dose_mg,patient)
        patient.receive(final_dose)
    
    
class Patient:
    def __init__(self, name):
        self.name = name
    
    def receive(self, dose):
        print(f"{self.name} received {dose}mg")

class StandardDosingPolicy:
    def calculate(self,dose,patient):
        return dose
    
class PediatricDosingPolicy:
    def calculate(self, dose, patient):
        return dose * 0.5

order = MedicationOrder(
    base_dose_mg=100,
    dosing_policy=PediatricDosingPolicy()
)

patient = Patient("John Doe")
order.administer(patient)
