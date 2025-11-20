# Methods + business logic (BMI, validation, etc.)

class Patients():
    count = 0
    registry = []
    def __init__(self, name, age, weight, height):
        self.name = name
        
        self.__age = None
        self.__weight = None
        self.__height = None
        
        self.age = age
        self.weight = weight
        self.height = height
        Patients.count +=1

        
        
    @property
    def weight(self):
                return self.__weight
    @weight.setter
    def weight(self, value):
        if not isinstance (value,(int,float)):
            raise ValueError("Weight must be a number")
        if not (1 <= value <= 500):
            raise ValueError("Weight must be betw 1 and 500 kg")
        self.__weight = float(value)
                
                
    @property
    def height(self):
        return self.__height
            
    @height.setter
    def height(self, value):
        if not isinstance (value,(int,float)):
            raise ValueError("height must be a number")
        if not (0.5<= value <= 2.5):
            raise ValueError("height must be betw 1 and 20 m")
        self.__height = float(value)
            
    @property
    def age(self):
        return self.__age
            
            
    @age.setter
    def age(self, value):
        if not isinstance (value,int):
            raise ValueError("age must be a number")
        if not (0 <= value <= 120):
            raise ValueError("age must be betw 1 and 120 years")
        self.__age = value
                
            
    @property
    def bmi(self):
        return round(self.weight / (self.height**2) ,2)
    
    @property
    def category_bmi(self):
        bmi = self.bmi
        if bmi < 18.5:
            return "underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi <30:
            return "overweight"
        elif bmi >=30:
            return "obese"
        
    @classmethod
    def identify_by_name(cls,name):
        return [p for p in cls.registry if p.name.lower() == name.lower()]
    
    @classmethod
    def overweight_patients(cls):
        return [p for p in cls.registry if p.category_bmi in ("overweight", "obese")]
   
               
p = Patients("Collan", 21, 49, 1.2)
p1 = Patients("Collan", 21, 71, 1.74)
p2 = Patients("Amos", 34, 95, 1.80)
p3 = Patients("Sarah", 19, 48, 1.60)
p4 = Patients("Joy", 45, 110, 1.65)
p5 = Patients("Brian", 29, 60, 1.2)

print(f"total patients: {Patients.count}")

print("\nAll overweight and obese patients")
for p in Patients.overweight_patients():
    print(p.name, p.bmi, p.category_bmi)

print("\nSearch for 'Amos':")
for p in Patients.identify_by_name("Amos"):
    print(p.name, p.age, p.bmi)