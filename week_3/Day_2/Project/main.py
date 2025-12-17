# we need a definition of a patient, a storage mechanism, and brain to contol rules

from models.patients import Patient
from storage.patient_csv_repository import PatientCSVRepository
from services.patient_service import PatientService

repos = PatientCSVRepository("patients.csv")#lets choose csv as storage
service = PatientService(repos)# the brain

p1 = Patient("p001", "Collan", 21)#this patient exists only in RAM

service.regiter_patient(p1)# officially adds this patient

for patient in service.list_patients():#gimme all pat urrently store
    print(patient.patient_id, patient.name, patient.age)#display this way
    