"""Adapter Pattern- Intergration lies detector
Adapters normalize shapes not meaning
Clinical risk :
Adapters are where  reality gets rewritten and every rewrite must leave a scar"""

from typing import Dict, Any, List
from datetime import datetime



class LabResult:
    def __init__(
        self,
        patient_id:str,
        test_name:str,
        value:float,
        unit:str,
        collected_at:datetime,
        warnings:List[str],
        source:str
    ):
        self.patient_id= patient_id
        self.test_name = test_name
        self.value = value
        self.unit = unit
        self.collected_at = collected_at
        self.warnings = warnings
        self.source = source
    
    def as_dict(self)->Dict[str,any]:
        return{
            "patient_id": self.patient_id,
            "test_name": self.test_name,
            "value": self.value,
            "unit": self.unit,
            "collected_at": self.collected_at.isoformat(),
            "warnings": self.warnings,
            "source": self.source,
        }
   
   
        
class Adapter:
    """translators"""
    def adapt(self, raw:Dict[str,any])->LabResult:
        raise NotImplementedError
    
"""
System A format:
    {
         "pid": "123",
        "test": "Glucose",
        "result_mg_dl": 180,
        "timestamp": "2026-02-01T08:30:00"   
    }
"""


class SystemAdapter(Adapter):
    def adapt(self, raw:Dict[str,any])-> LabResult:
        warnings= []
        unit = "mg/dl"
        warnings.append("unit fixed to mg/dl(no alternative units supported)")
        
        try:
            collected_at = datetime.fromisoformat(raw["timestamp"])
        except Exception:
            warnings.append("invalid timestamp formatdefaulting to ingestion time")
            collected_at= datetime.utcnow()
        
        return LabResult(
            patient_id=raw["pid"],
            test_name=raw["test"],
            value=float(raw["result_mg_dl"]),
            unit =unit,
            collected_at=collected_at,
            warnings=warnings,
            source="SystemA"
        )
        


"""
System B format:
{
    "patient": "123",
    "analyte": "Glucose",
    "value": 9.9,
    "unit": "mmol/L",
    "date_collected": "01-02-2026"
}
"""

class SystemBAdapter:
    def adapt(self, raw:Dict[str,any]):
        warnings = []
        #converting mmol/l to mg/dl
        if raw["unit"] == "mmol/L":
            warnings.append("Value converted from mmol/L to mg/dl using factor 18.0")
            
            value=raw["value"]*18.0
            unit="mg/dl"
        else:
            raise ValueError(
                "Unknown unit adapter refuses to guess"
            )
            
        try:
            collected_at=datetime.strptime(
                raw["date_collected"], "%d-%m--%Y"
            ).replace(hour=12)
            warnings.append("No collection time provided, assumed 12:00")
        except Exception:
            warnings.append("Invalid timestamp formatdefaulting to ingestion time ")
            collected_at=datetime.utcnow()
        
        return LabResult(
            patient_id=raw["patient"],
            test_name=raw["analyte"],
            value=value,
            unit=unit,
            collected_at=collected_at,
            warnings=warnings,
            source="SystemB"
        )
        


if __name__=="__main__"    :
    system_a_payload= {
        "pid": "123",
        "test": 'glucose',
        'result_mg_dl': 180,
        'timestamp':"2026-02-01T08:30:00"
        
    }
    
    system_b_payload = {
        "patient": "123",
        "analyte": "Glucose",
        "value": 9.9,
        "unit": "mmol/L",
        "date_collected": "01-02-2026"
    }
    a = SystemAdapter().adapt(system_a_payload)
    b = SystemBAdapter().adapt(system_b_payload)

    print(a.as_dict())
    print(b.as_dict())            