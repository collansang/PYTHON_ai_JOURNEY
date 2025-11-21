#for mode details on mini project check notes

class Patient:
    ALLOWED_FIELDS = {"name", "age", "weight", "height", "assigned_doc"}
    def __init__(self, pat_id, name, age, weight, height, assigned_doc = None):
        self.name = name
        self.id = pat_id
        
        self.__age = None
        self.__weight = None
        self.__height = None
     
        
        
        self.age = age
        self.weight = weight
        self.height = height
        
        self.med_hx = []
        
    def update_patient(self, **kwargs):
        for field, value in kwargs.items():
            if field not in Patient.ALLOWED_FIELDS:
                raise AttributeError(f"Cannot update field ; {field}")
            setattr (self, field, value)
        
    @property
    def bmi(self):
        return round(self.weight / (self.height**2), 2)
    
    
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, value):
        if not isinstance (value, int):
            raise ValueError( "age must be a number")
        if not (0<= value <=120):
            raise ValueError( "age not ralistic")
        self.__age = value
        
    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self,value):
        if not isinstance (value,(int, float)):
            raise ValueError( "weight must be a number")
        if not (1<= value <= 500):
            raise ValueError( "weight out of range")
        self.__weight = value
        
    @property
    def height(self):
        return self.__height
    @height.setter
    def height(self, value):
        if not isinstance (value, (int, float)):
            raise ValueError( "height must be a number")
        if not (0.5 <= value <= 2.5):
            raise ValueError( "height out of range")
        self.__height = value


class Doctor:
    def __init__(self, doctor_id, name, speciality):
        self.doctor_id = doctor_id
        self.name = name
        self.speciality = speciality
        
        self.patients = []
        
    def add_patients(self, patient):
        if patient not in self.patients:
            self.patients.append(patient)
            
    def list_patients(self):
        return [p.name for p in self.patients]
    
    def update_patient(self, pat_id, **updates):
        patient = next((p for p in self.patients if p.id == pat_id), None)
        if not patient:
            raise  ValueError("patient not found under this doctor")
        patient.update_patient(**updates)
        
        
        
        
patients = [
    Patient(1, "John", 30, 70, 1.75),
    Patient(2, "Sarah", 28, 60, 1.6),
    Patient(3, "Mike", 40, 80, 1.8)
]


for patient in patients:
    print(f"ID: {patient.id}, Name: {patient.name}, Age: {patient.age}, "
          f"Weight: {patient.weight}kg, Height: {patient.height}m, BMI: {patient.bmi}")

