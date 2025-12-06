#ConflictErrors - opposite of NotFoundErrors
# The thing exists but it couses conflict, violates rules
#Examples:
        # Two patients with same id
        #Trying o register a doctor who already exists
        #Prescribing a drig A that  clashes with drug B the patient is already taking
        #double booking an appointment 
#Errors defined here:
    #1. ConflictErrors - defines the exceptions related to conflict
    #2. DuplicatePatientError - raised when trying to register a patient with an existing id
    #3. DuplicateDoctorError - raised when tring to register a doctor with an existing id
    #4. AppointmentConflictError - raised when trying to book an appointment that conflicts with an existing one
    #5. MedicationConflictError - raised when prescribing two that clash/ contradicts each other
    #6. ResourceConflictError - error based on resources conflict, ie bed already occupied, x-ray machine already in use etc
    #7. StateconflictError - error based on conflicting state, ie trying to discharge a patient who is not admitted yet, assigning a doctor who is on leave, or scheduling surgery for a patient already in surgery


class HospitalError(Exception):
    """Base class for all hospital related exceptions"""
    pass

class ConflictError(HospitalError):
    """Base class for all conflict related errors"""
    pass

class DuplicatePatientError(ConflictError):
    pass

class DuplicateDoctorError(ConflictError):
    pass

class AppointmentConflictError(ConflictError):
    pass

class MedicationConflictError(ConflictError):
    pass

patients = {
    'p001' : {'name' : 'John Wafula', 'age' : 32},
    'p002' : {'name' : 'Mary Wanjiku', 'age' : 23},
    'p003' : {'name' : 'Moses Kipchirchir' , 'age' : 21}
}

doctors = {
    'd001' : {'name' : 'Dr. Sofie', 'specialty' : 'Cardiology'},
    'd002' : {'name' : 'Dr. Sang', 'specialty' : 'Neurology'},
    'd003' : {'name' : 'Dr. Brown', 'specialty' : 'Pediatrics'}
}

appointment = {
    'a001' : {'patient_id' : 'p001', 'doctor_id' : 'd001', 'date' : '2025-10-01'},
    'a002' : {'patient_id' : 'p002', 'doctor_id' : 'd002', 'date' : '2025-10-05'},
    'a003' : {'patient_id' : 'p003', 'doctor_id' : 'd003', 'date' : '2025-10-09'}
}


def register_patient(patient_id: str, name : str, age : int):
    if patient_id in patients:
        raise DuplicatePatientError(f"Patient with id {patient_id} already exists.")
    patients[patient_id]= {'name' : name, 'age' : age}

def register_doctor(doctor_id: str, name : str, specialty : str):
    if doctor_id in doctors:
        raise DuplicateDoctorError(f"Doctor with id {doctor_id} already exists.")
    doctors[doctor_id] = {'name' : name, 'specialty' : specialty}
    
def book_appointment(appointment_id : str, patient_id : str, doctor_id :str, date : str):
    for apt in appointment.values():
        if apt["doctor_id"] == doctor_id and apt["date"] == date:
            raise AppointmentConflictError(f"Doctor {doctor_id} already has an appointment on {date}.")
    appointment[appointment_id] = {'patient_id' : patient_id, 'doctor_id': doctor_id, 'date' : date}
        
def prescribe_medication(patient_id : str, medication_a : str, medication_b : str):
    conflicting_meds = {("drugA", "drugB"), ("drugC", "drugD")}
    a = medication_a.lower()
    b = medication_b.lower()
    if (a, b) in conflicting_meds or (b, a) in conflicting_meds:
        raise MedicationConflictError(f"Medications{medication_a}and {medication_b} conflict each other for patient{patient_id}")
    print(f"Medications {medication_a} and {medication_b} prescribed to patient {patient_id} successfully.")
    
    
    
def main():
    try:
        register_patient('p001', 'Alice', 22)
    except DuplicatePatientError as e:
        print(f"Duplicate patient error: {e}")
    except ConflictError as e:
        print(f"Conflict error: {e}")
    except HospitalError as e:
        print(f"Hospital error: {e}")  
    
    try:
        register_doctor('d001', 'Dr. Smith', 'Dermatology')
    except DuplicateDoctorError as e:
        print(f"Duplicate doctor error: {e}")
    except ConflictError as e:
        print(f"Conflict error: {e}")
    except HospitalError as e:
        print(f"Hospital error: {e}")
    
    try:
        book_appointment('a004', patient_id='p002', doctor_id='d002', date='2025-10-05')
    except AppointmentConflictError as e:
        print(f"Appointment conflict error: {e}")
    except ConflictError as e:
        print(f"Conflict error: {e}")
    except HospitalError as e:
        print(f"Hospital error: {e}")
        
main()