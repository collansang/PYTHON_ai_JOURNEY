from abc import ABC, abstractmethod

class DosingPolicy(ABC):
    @abstractmethod
    def calculate(self, base_dose_mg: float, patient) -> float:
        pass

    @abstractmethod
    def name(self) -> str:
        pass
class MedicationOrder:
    def __init__(self, base_dose_mg: float, dosing_policy: DosingPolicy):
        if base_dose_mg <= 0:
            raise ValueError("Base dose must be positive")

        self.base_dose_mg = base_dose_mg
        self.dosing_policy = dosing_policy

    def administer(self, patient):
        final_dose = self.dosing_policy.calculate(self.base_dose_mg, patient)

        if final_dose <= 0:
            raise ValueError("Calculated dose must be positive")

        patient.receive_dose_mg(final_dose)

        self._audit(patient, final_dose)

    def _audit(self, patient, final_dose):
        print(
            f"[AUDIT] {self.dosing_policy.name()} | "
            f"Base: {self.base_dose_mg} mg → Final: {final_dose} mg"
        )

class StandardDosingPolicy(DosingPolicy):
    def calculate(self, base_dose_mg, patient):
        return base_dose_mg

    def name(self):
        return "Standard Adult Dosing"
class Patient:
    def receive_dose_mg(self, dose_mg: float):
        print(f"Patient received {dose_mg} mg")
