# === EXCEPTIONS ===

class HospitalError(Exception):
    """Base class for all hospital-related exceptions."""
    pass

class ValidationError(HospitalError):
    pass

class PatientValidationError(ValidationError):
    pass

class VitalsValidationError(ValidationError):
    pass

def validate_patient(name: str, age : int):
    """Registers patients after validating them"""
    if not name or not isinstance(name, str):
        raise PatientValidationError("patient must be a non-empty string")
    
    if not isinstance(age, int):
        raise PatientValidationError(f"{age} Age must be an integer)")
    
    
    if not (0< age< 120):
        raise PatientValidationError(f"{age} Age out of range (0-20)") 



def validate_vitals(temperature : float, heart_rate : int):
    """Validates pFGTRGUJ769I8ls"""
    if not (34 <= temperature <= 42):
        raise VitalsValidationError(f"{temperature} Temperature out of range (34 - 42")
    
    if not (30 <= heart_rate <=200):
        raise VitalsValidationError(f"{heart_rate} Heart Rate out of range (30 - 200)")



def register_patient(name , age, temperature, heart_rate : int):
    try:
        validate_patient(name, age)
        validate_vitals(temperature, heart_rate)
        
        print(f"Patient {name} registered successfully.")
        
    except PatientValidationError as e:
        print(f"Patient validation Error: {e}")
    except VitalsValidationError as e:
        print(f"Vitals validation Error: {e}")
    except ValidationError as e:
        print(f"Validation Error: {e}")
    except HospitalError as e:
        print(f"Hospital Error: {e}")
        
        




register_patient("", 30, 37.0, 80)          # name invalid
register_patient("John", 200, 37.0, 80)     # age invalid
register_patient("Jane", 25, 60.0, 80)      # temperature invalid
register_patient("Abe", 40, 37.0, 300)      # heart rate invalid
register_patient("Mary", 40, 37.0, 90)      # success



