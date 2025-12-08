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
    'p001': {'role': 'patient'},  # Added patient users
    'p002': {'role': 'patient'},
    'p003': {'role': 'patient'}
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

appointments = {  # Changed from 'appointment' to 'appointments'
    'a001': {'patient_id': 'p001', 'doctor_id': 'd001', 'date': '2025-10-01', 'status': 'scheduled'},
    'a002': {'patient_id': 'p002', 'doctor_id': 'd002', 'date': '2025-10-05', 'status': 'scheduled'},
    'a003': {'patient_id': 'p003', 'doctor_id': 'd003', 'date': '2025-10-09', 'status': 'scheduled'}
}


def validate_patient(name: str, age: int):
    """Validate patient data"""
    if not name or not isinstance(name, str):
        raise PatientValidationError("Patient name must be a non-empty string")
    
    if not isinstance(age, int):
        raise PatientValidationError(f"Age must be an integer, got {type(age)}")
    
    if not (0 < age < 120):
        raise PatientValidationError(f"Age {age} is out of valid range (0-120)")


def validate_appointment(patient_id: str, doctor_id: str, date: str):
    """Validate appointment data"""
    if not patient_id or patient_id not in patients:
        raise AppointmentValidationError(f"Invalid patient ID: {patient_id}")
    
    if not doctor_id or doctor_id not in doctors:
        raise AppointmentValidationError(f"Invalid doctor ID: {doctor_id}")
    
    if not date or not isinstance(date, str):
        raise AppointmentValidationError("Date must be a non-empty string")
    
    # Simple date format validation (you could add more sophisticated validation)
    try:
        year, month, day = map(int, date.split('-'))
        if not (1 <= month <= 12 and 1 <= day <= 31):
            raise ValueError
    except (ValueError, AttributeError):
        raise AppointmentValidationError(f"Invalid date format: {date}. Use YYYY-MM-DD")


def register_patient(patient_id: str, name: str, age: int):
    """Register a new patient"""
    if patient_id in patients:
        raise DuplicatePatientError(f"Patient with ID {patient_id} already exists.")
    
    validate_patient(name, age)
    patients[patient_id] = {'name': name, 'age': age}
    
    # Also create a user account for the patient
    users[patient_id] = {'role': 'patient'}
    
    print(f"Patient {name} registered successfully with ID {patient_id}")
    return patient_id


def register_doctor(doctor_id: str, name: str, specialty: str):
    """Register a new doctor"""
    if doctor_id in doctors:
        raise DuplicateDoctorError(f"Doctor with ID {doctor_id} already exists.")
    
    if not name or not isinstance(name, str):
        raise ValidationError("Doctor name must be a non-empty string")
    
    doctors[doctor_id] = {'name': name, 'specialty': specialty}
    print(f"Doctor {name} registered successfully with ID {doctor_id}")
    return doctor_id


def book_appointment(appointment_id: str, patient_id: str, doctor_id: str, date: str):
    """Book a new appointment"""
    if appointment_id in appointments:
        raise DuplicateAppointmentError(f"Appointment ID {appointment_id} already exists.")
    
    # Validate appointment data
    validate_appointment(patient_id, doctor_id, date)
    
    # Check for scheduling conflicts
    for apt_id, apt in appointments.items():
        if apt["doctor_id"] == doctor_id and apt["date"] == date and apt["status"] != "cancelled":
            raise AppointmentConflictError(f"Doctor {doctor_id} already has an appointment on {date}.")
    
    appointments[appointment_id] = {
        'patient_id': patient_id,
        'doctor_id': doctor_id,
        'date': date,
        'status': 'scheduled'
    }
    
    print(f"Appointment {appointment_id} booked successfully for {date}")
    return appointment_id


def require_role(user_id: str, allowed_roles: list[str]):
    """Check if user has required role"""
    if user_id not in users:
        raise AuthorizationError(f"User {user_id} not found")
    
    user_role = users[user_id]["role"]
    
    if user_role not in allowed_roles:
        raise RolePermissionError(f"Role '{user_role}' is not allowed. Allowed roles: {allowed_roles}")


def access(user_id: str):
    """Check if user has access"""
    if user_id not in users:
        raise AuthorizationError(f"User {user_id} not logged in or does not exist")


def check_ownership(user_id: str, resource_type: str, resource_id: str):
    """Check if user owns a resource"""
    access(user_id)  # First check if user exists
    
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


class PatientState:
    """Patient state machine implementation"""
    VALID_TRANSITIONS = {
        'registered': ['admitted'],
        'admitted': ['discharged'],
        'discharged': []
    }
    
    def __init__(self, patient_id: str, name: str):
        self.patient_id = patient_id
        self.name = name
        self.state = 'registered'
        
    def transition(self, new_state: str):
        """Transition to a new state"""
        if self.state == new_state:
            raise AlreadyInStateError(f"Patient is already in state: {self.state}")
        
        allowed_transitions = self.VALID_TRANSITIONS.get(self.state, [])
        
        if new_state not in allowed_transitions:
            raise InvalidTransitionError(
                f"Cannot transition from '{self.state}' to '{new_state}'. "
                f"Allowed transitions: {allowed_transitions}"
            )
        
        old_state = self.state
        self.state = new_state
        print(f"Patient {self.name} transitioned from {old_state} to {new_state}")
        return self.state
    
    def admit(self):
        """Admit the patient"""
        return self.transition('admitted')
    
    def discharge(self):
        """Discharge the patient"""
        return self.transition('discharged')
    
    def __str__(self):
        return f"Patient {self.name} (ID: {self.patient_id}) - State: {self.state}"


# Example usage and testing
if __name__ == "__main__":
    try:
        # Test patient registration
        print("=== Testing Patient Registration ===")
        register_patient('p004', 'Alice Johnson', 28)
        
        # Test duplicate patient error
        try:
            register_patient('p001', 'Duplicate John', 40)
        except DuplicatePatientError as e:
            print(f"Caught expected error: {e}")
        
        # Test validation error
        try:
            register_patient('p005', '', 150)
        except PatientValidationError as e:
            print(f"Caught expected error: {e}")
        
        # Test appointment booking
        print("\n=== Testing Appointment Booking ===")
        book_appointment('a004', 'p001', 'd001', '2025-10-10')
        
        # Test appointment conflict
        try:
            book_appointment('a005', 'p002', 'd001', '2025-10-01')
        except AppointmentConflictError as e:
            print(f"Caught expected error: {e}")
        
        # Test role-based access
        print("\n=== Testing Role-Based Access ===")
        require_role('admin1', ['admin', 'reception'])
        print("Admin access granted")
        
        try:
            require_role('doc1', ['admin', 'reception'])
        except RolePermissionError as e:
            print(f"Caught expected error: {e}")
        
        # Test patient state machine
        print("\n=== Testing Patient State Machine ===")
        patient = PatientState('p001', 'John Wafula')
        print(patient)
        
        patient.admit()
        print(patient)
        
        patient.discharge()
        print(patient)
        
        # Test invalid transition
        try:
            patient.admit()
        except InvalidTransitionError as e:
            print(f"Caught expected error: {e}")
        
        # Test ownership check
        print("\n=== Testing Ownership ===")
        check_ownership('p001', 'appointment', 'a001')
        print("Patient p001 owns appointment a001 - Access granted")
        
        try:
            check_ownership('p002', 'appointment', 'a001')
        except OwnershipError as e:
            print(f"Caught expected error: {e}")
        
    except HospitalError as e:
        print(f"Unexpected hospital error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")