import json
from pathlib import Path
from models.patient import Patient

DATA_PATH = Path("data/patients.json")

class PatientRepository:
    def _load_raw(self):#we first check path and  load the existing data
        if not DATA_PATH.exists():
            return[]
        with DATA_PATH.open("r", "utf-8") as file:
            return json.load(file)
    def _save_raw(self, raw: list):#writes raw data to json file
        DATA_PATH.parent.mkdir(exist_ok = True)
        with DATA_PATH.open("w", encoding = "utf-8")as file:
            json.dump(raw, file, indent = 2)
            
    def _load_all(self):#gets all patients as python object, not raw data because from_dict
        raw = self._load_raw()
        return [Patient.from_dict(d) for d in raw]
    
    def _save_all(self, patients :list[Patient]):#saves all patients objects to file
        raw = [p.to_dict() for p in patients]
        self._save_raw(raw)
        
        
    