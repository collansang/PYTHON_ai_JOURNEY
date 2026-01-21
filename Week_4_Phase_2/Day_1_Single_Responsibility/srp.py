import json
from datetime import datetime

class Patient:
    def __init__(self, pid, name, age, height, weight):
        self.pid= pid
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    
class ClinicalVisits:
    def __init__(self, symptoms, diagnosis,visit_date):
        self.symptoms = symptoms
        self.diagnosis = diagnosis
        self.visit_date = visit_date
        
class BMICalculation:
    @staticmethod
    def calculate_bmi(weight: float, height: float):
        if isinstance(height,(int,float))and height> 0 :
            return round(weight / (height **2), 2)
        else:
            raise ValueError("Height Must be a positive number")
        
class RiskAssessment:
    @staticmethod
    def assess_risk(bmi:float, age:int):
        if age <45:
            if bmi < 22.0:
                return "Low Risk"
            elif 22.0 <= bmi <27.5:
                return "Moderate risk"
            else:
                return "High Risk"
        else:
            if age >= 45:
                if bmi < 22.0:
                    return "Moderate risk"
                elif 22.0 <= bmi < 27.5:
                    return "High risk"
                
                else:
                    return "Very High Risk"
                
class VisitsRecord:
    def __init__(self):
        self.records = records=[]
        
    def add_visit(self, visit: ClinicalVisits):
        self.records.append(visit)
        
    def add_to_file(self, filename: str):
        with open (filename, "w") as file:
            json.dump({
                "visits": [
                    {
                        "symptoms": visit.symptoms,
                        "diagnosis": visit.diagnosis,
                        "visit_date": visit.visit_date.strftime("%Y-%m-%d")
                    } for visit in self.records
                ]
            } , file)
            
class PatientSummary:
    @staticmethod
    def generate_summary(patient: Patient, bmi: float, risk_level: str, visits: VisitsRecord):
        summary = f"Patient Summary for {patient.name} (PID: {patient.pid})\n"
        summary += f"Age: {patient.age}, Height: {patient.height} m, Weight: {patient.weight} kg\n"
        summary += f"BMI: {bmi}, Risk Level: {risk_level}\n"
        summary += "Clinical Visits:\n"
        for visit in visits.records:
            summary += f"- Date: {visit.visit_date.strftime('%Y-%m-%d')}, Symptoms: {visit.symptoms}, Diagnosis: {visit.diagnosis}\n"
        return summary