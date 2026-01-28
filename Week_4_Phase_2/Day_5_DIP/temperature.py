from abc import ABC, abstractmethod

class FeverPolicy(ABC):
    @abstractmethod
    def threshold(self) -> float:
        pass
    
class AdmissionDecision:
    def __init__(self, fever_policy:FeverPolicy):
        self.fever_policy = fever_policy
        
    def should_admit(self, patient):
        return patient.temperature >= self.fever_policy.threshold()
    
class AdultFeverPolicy(FeverPolicy):
    def threshold(self):
        return 38.0
class ChildFeverPolicy(FeverPolicy):
    def threshold(self):
        return 37.5

policy = AdultFeverPolicy()
admission = AdmissionDecision(policy)
patient = type('Patient', (object,), {'temperature': 39.0})()  # Example patient object
decission = admission.should_admit(patient)
print(decission)  # Output: True

policy = ChildFeverPolicy()
admission = AdmissionDecision(policy)
patient = type('Patient', (object,), {'temperature': 37.0})()  # Example patient object
decission = admission.should_admit(patient)
print(decission)  # Output: False