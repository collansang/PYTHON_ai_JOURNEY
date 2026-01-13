from patient_repository import PatientRepository
from patient import Patient
import pickle


    
class PatientPickleRepository(PatientRepository):#I obey the repository contract
    def __init__(self, file_path):#storage location
        self.file_path = file_path
        
    def save(self, patient):
        patients = self.list_all()#load all the existing frozen patients
        patients.append(patient)#update the list
        with open(self.file_path, "wb") as file:#open the file in write binary mode
            pickle.dump(patients, file)#freeze the updated list into the file
            
    def list_all(self):
        try:
            with open(self.file_path, "rb") as file:#open freezer in binary read mode
                patient = pickle.load(file)#object rebuild exactly as they were
                return patient
        except FileNotFoundError:
            return []