#1. NotFoundErrors  is a base class for missing resources
#2. PatientNotFoundError used when searching patient by name or id
#3. DoctorNotFounfError used when:
                                #searching doctor by name or id
                                #assigning doctor to patient
                                #scheduling appointment with doctor
                                #looking up doctors shift
#4. AppointmentNotFoundError - used when:
                                        # searching appointment by id
                                        #cancelling appoint that does not exist
                                        #Trying to update a deleted appointment



class HospitalError(Exception):
    """base class for all hospital related errors"""
    pass

class NotFoundError(HospitalError):#in this case we are writting this after validation errors, so ic could go below it if we were writting in one bog code file
    """Base class for all not found errors"""
    pass

class PatientNotFoundError(NotFoundError):
    """class for patient not found errors"""
    pass

class DoctorNotFoundError(NotFoundError):
    """class for doctor not found errors"""
    pass

class AppointmentNotFoundError(NotFoundError):
    """class for missing appointment errors"""
    pass

patients = {
    'p001' : {'name' : 'John Wafula', 'Age' : 32},
    'p002' : {'name' : 'Mary Wanjiku', 'age' : 23},
    'p003' : {'name' : 'Moses Kipchirchir' , 'age' : 21}
}
doctors = {
    'd001' : {'name' : 'Dr. Sofie', 'specialty' : 'Cardiology'},
    'd002' : {'name' : 'Dr. Sang', 'specialty' : 'Neurology'},
    'd003' : {'name' : 'Dr. Brown', 'specialty' : 'Pediatrics'}
}
appointments = {
    'a001' : {'patient_id' : 'p001', 'doctor_id' : 'd001', 'date' : '2025-10-01'},
    'a002' : {'patient_id' : 'p002', 'doctor_id' : 'd002', 'date' : '2025-10-05'},
    'a003' : {'patient_id' : 'p003', 'doctor_id' : 'd003', 'date' : '2025-10-09'}
}

def Find_patient_by_id(patient_id : str):
    if patient_id not in patients:
        raise PatientNotFoundError(f"Patient with id {patient_id} not found.")
    return patients[patient_id]


def find_doctor_by_id(doctor_id : str):
    if doctor_id not in doctors:
        raise DoctorNotFoundError(f"Doctor with id {doctor_id} not found.")
    return doctors[doctor_id]


def Find_appointment_by_id(appointment_id : str):
    if appointment_id not in appointments:
        raise AppointmentNotFoundError(f"Appointment with id {appointment_id} not found.")
    return appointments[appointment_id]




def main():
    try:
        patient = Find_patient_by_id('p011')
        
    except PatientNotFoundError as e:
        print(f"Patient Not Found Error: {e}")
    except NotFoundError as e:
        print(f"Not found Error: {e}")
    except HospitalError as e:
        print(f"General Hospital Error: {e}")
        
    
    try:
        doctor = find_doctor_by_id('d010')
    except DoctorNotFoundError as e:
        print(f"Doctor Not Found Error: {e}")
    except NotFoundError as e:
        print(f"Not found Error: {e}")
    except HospitalError as e:
        print(f"General Hospital Error: {e}")
    
    
    try:
        appointment = Find_appointment_by_id('a010')
        
    except AppointmentNotFoundError as e:
        print(f"Appointment Not Found Error: {e}")
    except NotFoundError as e:
        print(f"Not found Error: {e}")
    except HospitalError as e:
        print(f"General Hospital Error: {e}")
    

    
        
main()
    