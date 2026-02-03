from dataclasses import dataclass
from datetime import datetime

@dataclass(frozen=True)
class ValueWithProvenance:
    value: int
    source: str
    timestamp: datetime
    confidence: float


class PatientRepository:
    def get_age(self, patient_id: str) -> ValueWithProvenance:
        return ValueWithProvenance(
            value=67,
            source="EHR",
            timestamp=datetime.utcnow(),
            confidence=0.9
        )



repo = PatientRepository()
age = repo.get_age("patient-1")

print(age.value, age.source, age.confidence)
