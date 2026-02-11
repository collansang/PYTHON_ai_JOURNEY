from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class ClinicalMeasurement:
    name:str
    value:Optional[float]
    
    observed_at:Optional[datetime] #when measured
    available_at:Optional[datetime]#when system knew
    
    source_system:str #device, lab
    reliability:float
    
    missing_reason:Optional[str]
    supports_decision:str
    diagnosis_time:Optional[datetime]#to determine pre/post
    
    def is_missing(self) -> bool:
        return self.value is None
    
    def is_prediagnosis(self)->bool:
        if not self.diagnosis_time or not self.observed_at:
            return False
        return self.observed_at<= self.diagnosis_time



class ClinicalDataPipeline:
    def __init__(self):
        self.logs=[]
        
    def log(self,message:str):
        self.logs.append(message)
        
        
    """Step 1 ingest"""
    def ingest(self,measurement:ClinicalMeasurement):
        self.log(f"[INGEST] {measurement.name} from {measurement.source_system}")
        return measurement
    
    
    """step 2 Temporal gate"""
    def enforce_temporal_integrity(self, measurement:ClinicalMeasurement, decision_time):
        if not measurement.available_at:
            raise ValueError(" Missing available_at timestamp")
        if measurement.available_at>decision_time:
            raise ValueError(f" Data leakage: {measurement.name} not available at decision time")
        self.log(f"[TEMPORAL OK] {measurement.name}")
        return measurement
    
    """step 3 transformation"""
    def transform(self, measurement:ClinicalMeasurement):
        original_value = measurement.value
        
        if measurement.name == "glucose_mg_dl":
            measurement.value = measurement.value/18
            measurement.name = "glucose_mmol_l"
            self.log(
                f"[transform] converted glucose from {original_value}mg/dl to {measurement.value} mmol/l"
            )
        return measurement
    
    """validation step 4"""
    def validate(self, measurement:ClinicalMeasurement, min_reliability=0.7):
        if measurement.is_missing():
            if not measurement.missing_reason:
                raise ValueError("Missing value without a missing reason")
            self.log(f"[MISSING] {measurement.name} because {measurement.missing_reason}")
            return measurement
        
        if measurement.reliability<min_reliability:
            raise ValueError(f"Low reliability for {measurement.name}: {measurement.reliability}")
        self.log(f"[VALID] {measurement.name}")
        return measurement
    
 
 
        
 

pipeline = ClinicalDataPipeline()

m = ClinicalMeasurement(
    name="glucose_mg_dl",
    value=180,
    observed_at=datetime(2026, 2, 10, 10, 0),
    available_at=datetime(2026, 2, 10, 10, 5),
    source_system="LabSystemA",
    reliability=0.95,
    missing_reason=None,
    supports_decision="DKA triage",
    diagnosis_time=datetime(2026, 2, 11)
)

decision_time = datetime(2026, 2, 10, 11, 0)

m = pipeline.ingest(m)
m = pipeline.enforce_temporal_integrity(m, decision_time)
m = pipeline.validate(m)
m = pipeline.transform(m)

print(pipeline.logs)


    