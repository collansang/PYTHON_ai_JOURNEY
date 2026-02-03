from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Any

@dataclass(frozen=True)
class ProvenancedValue:
    value: Any
    source_system: str
    timestamp: datetime
    confidence: float
    
    def __post_init__(self):
        if not (0.0<=self.confidence<=1.0):
            raise ValueError("Confidence mus be between 0.0 and 1.0")
        
@dataclass(frozen=True)
class ProvenancedRecord:
    fields: Dict[str, ProvenancedValue]
    def get(self, field_name: str) -> ProvenancedValue:
        if field_name not in self.fields:
            raise KeyError(f"Field '{field_name}' not found with provenance")
        return self.fields[field_name]

class PatientRepository:
    def get_patient(self, patient_id: str)->ProvenancedRecord:
        raise NotImplementedError

class EHRPatientRepository(PatientRepository):
    def get_patient(self, patient_id:str)->ProvenancedRecord:
        now= datetime.utcnow()
        
        return ProvenancedRecord(
            fields= {
                "age": ProvenancedValue(value=67,
                                        source_system="Hospital_EHR_v3",
                                        timestamp=now,
                                        confidence=0.95
                                        ),
                "oxygen_saturation": ProvenancedValue(
                    value=89,
                    source_system="Bedside_Monitor_12A",
                    timestamp=now,
                    confidence=0.85
                ),
                "diagnosis_code": ProvenancedValue(
                    value="J96.00",
                    source_system="Clinician_Entered",
                    timestamp=now,
                    confidence=0.7
                )
                
            }
        )
            
            
if __name__ == "__main__":
    repo = EHRPatientRepository()
    patient = repo.get_patient("patient-123")
    
    o2 = patient.get('oxygen_saturation')
    
    print('o2:', o2.value)       
    print('source:', o2.source_system)       
    print('timestamp:', o2.timestamp)       
    print('confidence:', o2.confidence)       