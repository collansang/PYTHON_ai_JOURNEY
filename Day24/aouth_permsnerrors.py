#Authorization and Permision errors ensures that only authorized users can acess, insert, modify or delete resources

#Some  Hospitals strict rules:
    # Only admins can register doctors
    # Only doctors can prescribe medication
    # Only receptionists/admin can book appointments
    # Only staff assigned to a patient can modify patient data

#AuthorizationError - action denied because you are not logged in
#PermissionError - You are logged in but you cant do the action
#RolepermissionError - your role does not allow you to do the action
#OwnershipError - you can only access resources assigned to you
#AccessDeniedError - general error for access denied situations

"""PERMISION ERRORS"""
class HospitalError(Exception):
    """base for all hospital related errors"""
    pass

class AuthorizationError(HospitalError):
    """raised when user not logged in tries to access a resources"""
    pass

class PermissionError(HospitalError):
    """raised when a user lacks permission for a required action"""
    pass

class RolePermissionError(PermissionError):
    pass

class OwnershipError(PermissionError):
    pass

class AccessDeniedError(PermissionError):
    pass


"""CONFLICT ERRORS"""
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


users = {
    'admin1' : {'role' : 'admin'},
    'doc1' : {'role' : 'doctor'},
    'reception1' : {'role': 'reception'}
}


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



def require_role(user_id : str, allowed_role : list[str]):
    
    if user_id not in users:
        raise AuthorizationError(f"{user_id} not logged in or does not exist")
    
    user_role = users[user_id]["role"]
    
    if user_role not in allowed_role:
        raise RolePermissionError(f"Role '{user_role}' is not allowed to perform this action")
    

def register_patient(user_id : str, patient_id: str, name : str, age : int):
    require_role(user_id,["admin","reception"])
    if patient_id in patients:
        raise DuplicatePatientError(f"Patient with id {patient_id} already exists.")
    patients[patient_id]= {'name' : name, 'age' : age}

def register_doctor(user_id : str,doctor_id: str, name : str, specialty : str):
    if doctor_id in doctors:
        require_role(user_id,["admin"])
        raise DuplicateDoctorError(f"Doctor with id {doctor_id} already exists.")
    doctors[doctor_id] = {'name' : name, 'specialty' : specialty}
    
def book_appointment(user_id : str,appointment_id : str, patient_id : str, doctor_id :str, date : str):
    require_role(user_id,["reception", "admin", "doctor"])
    for apt in appointment.values():
        if apt["doctor_id"] == doctor_id and apt["date"] == date:
            raise AppointmentConflictError(f"Doctor {doctor_id} already has an appointment on {date}.")
    appointment[appointment_id] = {'patient_id' : patient_id, 'doctor_id': doctor_id, 'date' : date}
        
def prescribe_medication(user_id : str,patient_id : str, medication_a : str, medication_b : str):
    require_role(user_id,["doctor"])
    conflicting_meds = {("drugA", "drugB"), ("drugC", "drugD")}
    a = medication_a.lower()
    b = medication_b.lower()
    if (a, b) in conflicting_meds or (b, a) in conflicting_meds:
        raise MedicationConflictError(f"Medications{medication_a}and {medication_b} conflict each other for patient{patient_id}")
    print(f"Medications {medication_a} and {medication_b} prescribed to patient {patient_id} successfully.")
    
    
    
    
def main1():
    try:
        # FAIL: doctor trying to register another doctor
        register_doctor("doc1", "d004", "Dr. Alex", "Orthopedics")
    except RolePermissionError as e:
        print("Role error:", e)

    try:
        # FAIL: receptionist trying to prescribe medication
        prescribe_medication("reception1", "p001", "drugA", "drugB")
    except PermissionError as e:
        print("Permission error:", e)

    try:
        # FAIL: unknown user
        register_patient("unknown_user", "p010", "Alice", 32)
    except AuthorizationError as e:
        print("Authorization error:", e)

    try:
        # SUCCESS: admin registers a new doctor
        register_doctor("admin1", "d004", "Dr. Alex", "Orthopedics")
        print("Doctor registered successfully.")
    except HospitalError as e:
        print("Unexpected hospital error:", e)
main1()