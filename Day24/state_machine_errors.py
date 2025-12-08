#STATE MECHINE ERRORS
#The reason for this is that hospital system is full of statefull workflows
    # A patient can go from registered → admitted → discharged, but not backwards.
    # A lab test can go from ordered → processing → completed, but not directly from ordered → completed.
    # A surgical procedure cannot start if the patient is not prepped.
    
    
#HospitalError
    #2.StateMachineError = something in this       object's state is simply illegal and the system should have never allowed it
        #InvalidTransitionError = tried moving from state A - B but the transition does not exis
        #StateNotallowedError = tried a valid action but not allowed in current state
    
    

class HospitalError(Exception):
    pass

class StatemachineError(HospitalError):
    pass

class InvalidStateError(StatemachineError):
    pass


class InvalidTransitionError(StatemachineError):
    pass

class StateNotAllowedError(StatemachineError):
    pass

class Patient:
    VALID_PATIENTS = {
        'registered' : ['admitted'],
        'admitted': ['discharged'],
        'discharged' : [] 
    }
    
    def __init__(self, name):
        self.name =  name
        self.state = 'registered'
        
    def transition(self, new_state):
        allowed = Patient.VALID_PATIENTS[self.state]
        
        if new_state not in allowed:
            raise InvalidTransitionError(f"cannot move from {self.state} to {new_state}")
        
        self.state = new_state
        
    def discharge(self):
        if self.state != 'admitted':
            raise StateNotAllowedError(f"Dicharge only allowed in admitted, not in {self.state}")
        
        self.state = 'discharged'
        
def main():
    try:
        Patient.transition('discharged')
    except InvalidTransitionError as e:
        log(e)