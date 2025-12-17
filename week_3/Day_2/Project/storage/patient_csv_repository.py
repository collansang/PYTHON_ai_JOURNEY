import csv
from models.patients import Patient

class PatientCSVRepository:
    def __init__(self, file_path):
        self.file_path = file_path
        
    def save(self, patient:Patient):# lets store a Patient object
        with open(self.file_path, mode="a", newline='') as file:#open patient storage so i can add other patients, without destroying existing ones
            writer = csv.DictWriter(file,
                                    fieldnames=["patient_id", "name", "age"]
                                    )#this is like our header, guide. a structure
            if file.tell() == 0:#check cursor position if its at start( if this file is completely empty)
                writer.writeheader()# if so write the headlines/column names, if not just pass
            writer.writerow(patient.to_dict())# add the patients objets as dictionaries/ raw
            
    def get_all(self):
        patients= []# i dont know how many patients exist yet , but ill need somewhere to put them
        try:#the file might not exist, and thats normal
            with open(self.file_path, "r") as file:#open  the patien stiorage so i can read it
                reader = csv.DictReader(file)# ik each line rep 1 pat, i want each line as dict using header names
                for row in reader:# for every patient stored in the file...
                    patient = Patient.from_dict(row)#lets convert to real Patient object, here we convert strings to correct types, cornfirm.
                    patients.append(patient)# lets store out patient in our list
        except FileNotFoundError:#lets handle if file dows not exist
            pass
        return patients# now return all the patients in our list, including who we added, could be even zero
    