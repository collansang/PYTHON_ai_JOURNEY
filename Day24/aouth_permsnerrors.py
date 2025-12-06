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


users = {
    'admin1' : {'role' : 'admin'},
    'doc1' : {'role' : 'doctor'},
    'receptionist1' : {'role': 'reception'}
}


def check_authorization(is_logged_in : bool):
    if not is_logged_in:
        raise AuthorizationError("User must be loggin to perform the action")
    