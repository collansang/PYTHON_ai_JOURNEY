from enum import Enum
from abc import ABC, abstractmethod
from datetime import datetime
from datetime import timedelta
from unittest import result



class TemperatureStatus(Enum):
    NORMAL = "normal"
    LOW_GRADE_FEVER = "low_grade_fever"
    HIGH_GRADE_FEVER = "high_grade_fever"
    CRITICAL = "critical"
    

class ClinicalAction(Enum):
    OBSERVE = "observe"
    ADMIT = "admit"
    ICU = "icu"
    
    
class Clock(ABC):
    @abstractmethod
    def now(self) -> datetime:
        pass
    
    
class SystemClock(Clock):
    def now(self)-> datetime:
        return datetime.now()
    
    
class TemperatureReading:
    def __init__(self, value : float, measured_at: datetime):
        self.value = value
        self.measured_at = measured_at


class FeverPolicy(ABC):
    @abstractmethod
    def classify(self, tempertaure : float):
        pass
    
    @abstractmethod
    def recommended_action(self, status):
        pass
    
    @abstractmethod
    def max_temperature_age(self)-> timedelta:
        pass
   
    
class AdultFeverPolicy(FeverPolicy):
    def classify(self, temperature: float):
        if temperature < 37.5:
            return TemperatureStatus.NORMAL
        elif 37.5 <= temperature < 38.5:
            return TemperatureStatus.LOW_GRADE_FEVER
        elif 38.5 <= temperature < 40.0:
            return TemperatureStatus.HIGH_GRADE_FEVER
        else:
            return TemperatureStatus.CRITICAL
        
    def recommended_action(self, status):
        if status == TemperatureStatus.NORMAL:
            return ClinicalAction.OBSERVE
        elif status == TemperatureStatus.LOW_GRADE_FEVER:
            return ClinicalAction.OBSERVE
        elif status == TemperatureStatus.HIGH_GRADE_FEVER:
            return ClinicalAction.ADMIT
        else:
            return ClinicalAction.ICU
        
    def max_temperature_age(self) -> timedelta:
        return timedelta(hours=2)
 
    
class ChildFeverPolicy(FeverPolicy):
    def classify(self, temperature: float):
        if temperature < 37.0:
            return TemperatureStatus.NORMAL
        elif 37.0 <= temperature < 38.0:
            return TemperatureStatus.LOW_GRADE_FEVER
        elif 38.0 <= temperature < 39.5:
            return TemperatureStatus.HIGH_GRADE_FEVER
        else:
            return TemperatureStatus.CRITICAL
        
    def recommended_action(self, status):
        if status == TemperatureStatus.NORMAL:
            return ClinicalAction.OBSERVE
        elif status == TemperatureStatus.LOW_GRADE_FEVER:
            return ClinicalAction.OBSERVE
        elif status == TemperatureStatus.HIGH_GRADE_FEVER:
            return ClinicalAction.ADMIT
        else:
            return ClinicalAction.ICU
        
    def max_temperature_age(self) -> timedelta:
        return timedelta(hours=1)


class AdmissionDecision:
    def __init__(self, fever_policy: FeverPolicy, clock: Clock):
        self.fever_policy = fever_policy
        self.clock = clock
        
    def decide(self, temperature_reading: TemperatureReading):
        age = self.clock.now() - temperature_reading.measured_at
        if age > self.fever_policy.max_temperature_age():
            return {
                "error": "Temperature reading is too old to make a decision.",
                "action" : ClinicalAction.OBSERVE}
            
        
        status = self.fever_policy.classify(temperature_reading.value)
        action = self.fever_policy.recommended_action(status)
        return{
            "temperature": temperature_reading.value,
            "age_minutes" : age.total_seconds()/60,
            "status": status,
            "action": action,
            "policy": type(self.fever_policy).__name__
            
        }
        
        
clock = SystemClock()
policy = AdultFeverPolicy()
admission = AdmissionDecision(policy, clock)
temp = TemperatureReading(
    value= 39.5,
    measured_at= clock.now() - timedelta(minutes=30)
)
decision = admission.decide(temp)
print(decision)

result = admission.decide(temp)
print(result["status"].value)
print(result["action"].value)


policy = ChildFeverPolicy()
admission = AdmissionDecision(policy, clock)
temp = TemperatureReading(
    value= 38.0,
    measured_at= clock.now() - timedelta(minutes=90)
)
decision = admission.decide(temp)
print(decision)

