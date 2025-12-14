from services.patient_service import Patient_service

service = Patient_service

service.add_patient("john", 21, 34)
service.add_patient("collo", 26, 44)

for p in service.list_patients():
    print(p.name, p.age)