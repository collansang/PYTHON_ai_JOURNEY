from abc import ABC, abstractmethod

class SepsisScoringPolicy(ABC):
    @abstractmethod
    def calculate(self, measurements):
        pass
    
    @abstractmethod
    def get_core_system_name(self):
        pass
    
    @abstractmethod
    def is_applicable(self,measurements)->bool:
        pass
        

class SIRSPolicy(SepsisScoringPolicy):
    def __init__(self):
        self.criteria ={
            "temperature": (36, 38),
            "heart_rate": 90,
            "respiratory_rate":20,
            "pa_co2": 32,
            "wbc_count": (4.00, 12.0)
        }
    
    def calculate(self, measurements):
        fullfilled = []
        criteria_count = 0
        
        if measurements.temperature is not None:
            if measurements.temperature >= 38 or measurements.temperature <=36:
                criteria_count+=1
                fullfilled.append(f"heart_rate: {measurements.temperature} ℃")
                
        if measurements.heart_rate is not None and measurements.heart_rate>= 90:
            fullfilled.append(f"Heart_rate: {measurements.heart_rate} bpm")
            criteria_count+=1
            
        
        if measurements.respiratory_rate is not None and measurements.respiratory_rate>=20:
            fullfilled.append(f"Respiratory_rate: {measurements.respiratory_rate}/min")
            criteria_count+=1
        elif measurements.pa_co2 is not None and measurements.pa_co2 >32:
            fullfilled.append(f"pa_co2: {measurements.pa_co2}mmHg")
           
        if measurements.wbc_count is not None:
            if (measurements.wbc_count >=12 or measurements.wbc_count <=4):
                fullfilled.append(f"wbc_count: {measurements.wbc_count} cells")
                criteria_count+=1
        return BinaryScoreResult(criteris_met=criteria_count>=2,
                             fullfilled_criteria = fullfilled)
    def get_core_system_name(self):
        return "SIRS"   
    
    def is_applicable(self, measurements):
        required=[
            measurements.temperature,
            measurements.heart_rate,
            measurements.respiratory_rate,
            measurements.wbc_count
        ]
        return any(x is not None for x in required)
    

class qSOFAPolicy(SepsisScoringPolicy):
    def __init__(self):
        self.threshholds = {
            "repiratory_rate": 22,
            "systolic_bp": 100,
            "gcs" : 15
        }
        
        
    def calculate(self, measurements):
        points = 0
        if (measurements.respiratory_rate is not None and 
            measurements.respiratory_rate >= 22):
            points += 1
        
        if (measurements.gcs is not None and 
            measurements.gcs < 15):
            points += 1
        
        if (measurements.systolic_bp is not None and 
            measurements.systolic_bp <= 100):
            points += 1
        
        risk_level = "High" if points >= 2 else "Low"
        
        return RiskScoreResult(points=points,
            risk_level=risk_level
        )
    
    def get_name(self) -> str:
        return "qSOFA"
    def is_applicable(self, measurements):
        return all([
            measurements.respiratory_rate is not None,
            measurements.gcs is not None,
            measurements.systolic_bp is not None
        ])
        
        
        
        """service layer"""
        
class SepsisScoreService:
    def __init__(self):
        self._policies: dict[str,SepsisScoringPolicy] ={}
    def register_policy(self, policy: SepsisScoringPolicy):
        self._policies[policy.get_name()] = policy
    
    def get_available_policies(self, measurements):
        return [
            name for name, policy in self._policies.items()
            if policy.is_applicable(measurements)
        ]
    
    def calculate_score(self, 
                       policy_name: str, 
                       measurements):
        policy = self._policies.get(policy_name)
        if not policy:
            raise ValueError(f"Unknown policy: {policy_name}")
        
        if not policy.is_applicable(measurements):
            raise ValueError(f"Policy {policy_name} not applicable with given data")
        return policy.calculate(measurements)
        
    def calculate_all_applicable(self,measurements):
         
        results = {}
        for name, policy in self._policies.items():
            if policy.is_applicable(measurements):
                try:
                    results[name] = policy.calculate(measurements)
                except Exception as e:
                    print(f"Error calculating {name}: {e}")
        return results


def main():
    service= SepsisScoreService()
