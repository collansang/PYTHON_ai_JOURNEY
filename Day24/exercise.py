# Base Exception Hierarchy
class HospitalError(Exception):
    """Base class for all hospital-related exceptions"""
    pass


"""Validation errors"""
class ValidationError(HospitalError):
    pass

class PatientValidationError(ValidationError):
    pass

class AppointmentValidationError(ValidationError):
    pass


"""Not-Found errors"""
class NotFoundError(HospitalError):
    pass

class PatientNotFound(NotFoundError):
    pass

class DoctorNotFound(NotFoundError):
    pass

class AppointmentNotFound(NotFoundError):
    pass


"""Conflict errors"""
class ConflictError(HospitalError):
    pass

class DuplicatePatientError(ConflictError):
    pass

class DuplicateDoctorError(ConflictError):
    pass

class DuplicateAppointmentError(ConflictError):
    pass

class AppointmentConflictError(ConflictError):
    pass


"""Permission errors"""
class AuthorizationError(HospitalError):
    """For when user is not logged in or unknown"""
    pass

class PermissionError(AuthorizationError):
    """For when user is logged in but not allowed"""
    pass

class RolePermissionError(PermissionError):
    pass

class OwnershipError(PermissionError):
    pass

class AccessDeniedError(PermissionError):
    pass


"""State machine errors"""
class StateError(HospitalError):
    pass

class InvalidTransitionError(StateError):
    pass

class AlreadyInStateError(StateError):
    pass


# Data storage
users = {
    'admin1': {'role': 'admin'},
    'doc1': {'role': 'doctor'},
    'reception1': {'role': 'reception'},
    'p001': {'role': 'patient'}
}

patients = {
    'p001': {'name': 'John Wafula', 'age': 32},
    'p002': {'name': 'Mary Wanjiku', 'age': 23},
    'p003': {'name': 'Moses Kipchirchir', 'age': 21}
}

doctors = {
    'd001': {'name': 'Dr. Sofie', 'specialty': 'Cardiology'},
    'd002': {'name': 'Dr. Sang', 'specialty': 'Neurology'},
    'd003': {'name': 'Dr. Brown', 'specialty': 'Pediatrics'}
}

appointments = {
    'a001': {'patient_id': 'p001', 'doctor_id': 'd001', 'date': '2025-10-01', 'status': 'scheduled'},
    'a002': {'patient_id': 'p002', 'doctor_id': 'd002', 'date': '2025-10-05', 'status': 'scheduled'},
    'a003': {'patient_id': 'p003', 'doctor_id': 'd003', 'date': '2025-10-09', 'status': 'scheduled'}
}


"""VALIDATION OF PATIENT"""
def validate_patient(name : str, age :int):
    if not name or not isinstance(name,str):
        raise PatientValidationError("Patient name must be a non empty string")
    
    if not isinstance(age, int):
        raise PatientValidationError(f"Age must be an integer, got {type(age)}")
    if not (0< age <120):
        raise PatientValidationError(f"Age {age} is out of range (0-120)")
    
    
    """VALIDATING APPOINTMENT"""
def validate_appointment(patient_id : str, doctor_id : str,date:str):
    if not patient_id or patient_id not in patients:
        raise AppointmentValidationError(f"Invalid patient id {patient_id}")
    if not doctor_id or doctor_id not in doctors:
        raise AppointmentValidationError(f"Invalid doctor id {doctor_id}")
    if not date or not isinstance(date, str):
        raise AppointmentValidationError(f" Date must be a non-empty string")
    
    """Format date validation here"""
    try:
        year, month, day = map(int(date.split('-')))
        if not (1 <= month <= 12 and 1<= day <= 31):
            raise ValueError
            
    except (ValueError,AttributeError):
        raise AppointmentValidationError(f"Invalid date format {date}. use YYY-MM-DD")
    
    
def register_patient(patient_id: str, name : str, age: int):
    if patient_id in patients:
        raise DuplicatePatientError(f"Patient with id {patient_id} already exists")    
    validate_patient(name, age)
    patients[patient_id] = {'name': name, 'age': age}
    users[patient_id] = {'role':'patient'}
    print(f"Patient {name} registered successfully with id {patient_id}")
    
def register_doctor(doctor_id:str, name:str, specialty:str):
    if doctor_id in doctors:
        raise DuplicateDoctorError(f"Doctor with id {doctor_id} already exists")
    if not name or not isinstance(name,str):
        raise ValidationError("Doctor must be a non empty string")
    doctors[doctor_id] = {'name' : name, 'specialty':specialty}
    print(f"Doctor {name} is registered successfully with id {doctor_id}")
    
def book_appointment(appointment_id: str,patient_id:str, doctor_id:str, date : str):
    if appointment_id in appointments:
        raise DuplicateAppointmentError(f"Appointment ID {appointment_id} already exists")
    validate_appointment(patient_id,doctor_id,date)
    
    for apt_id,apt in appointments.items():
        if apt ['doctor_id'] == doctor_id and apt['date'] == date and apt['status'] != 'cancelled':
            raise AppointmentConflictError(f"Doctor{doctor_id} already has appointment on {date}")
    appointments[appointment_id]= {'patient_id':patient_id,
    'doctor_id' : doctor_id,
    'date' :date,
    'status': 'scheduled'
                                   }
    print(f"Appointment {appointment_id} vooked successfully for {date}")
    
def require_role(user_id:str ,allowed_roles:list[str]):
    if user_id not in users:
        raise AuthorizationError(f"User {user_id} not found")
    user_role = users[user_id]['role']
    if user_role not in allowed_roles:
        raise RolePermissionError(f"Role '{user_role}' is not allowed. Allowed roles: {allowed_roles}")

def access(user_id : str):
    if user_id not in users:
        raise AuthorizationError(f"User {user_id} not logged in or does not exist")
    
def check_ownership(user_id: str, resource_type: str, resource_id : str):
    access(user_id)
    if resource_type == 'patient':
        if user_id != resource_id and users[user_id]['role'] != 'admin':
            raise OwnershipError(f"User {user_id} does not own patient {resource_id}")
    
    elif resource_type == 'appointment':
        if resource_id not in appointments:
            raise AppointmentNotFound(f"Appointment {resource_id} not found")
        
        appointment = appointments[resource_id]
        if user_id != appointment['patient_id'] and user_id != appointment['doctor_id'] and users[user_id]['role'] != 'admin':
            raise OwnershipError(f"User {user_id} does not own appointment {resource_id}")
    
    else:
        raise AccessDeniedError(f"Cannot check ownership for resource type: {resource_type}")