#dunder str and dunder repr. str is printed by default but when absent repr is printed
#repr is mostly used in debugging to inspect the code
#the goal of str is to be readable
#the goal of repr is to be unambigous


class Patient:
    def __init__(self, name , age, weight):
        self.__name = None
        self.__age = None
        self.__weight = None
        
        self.name = name
        self.age = age
        self.weight = weight
    
    def __str__(self):
        return (f"Name : {self.name} age: {self.age}  weight: {self.weight}\n\n")
        

    
    
    def __repr__(self):
        return (f"name: {self.name!r} "
                f"age : {self.age!r} "
                f"weight : {self.weight!r}")
       
    
    @property
    def age(self):
        return self.__age 
    
        
    @age.setter
    def age(self, value):
        if not isinstance (value, int):
            raise ValueError("Age must be a number")
        if not (0 < value <= 120):
            raise ValueError("Age is unrealistic")
        self.__age = value
        
    @property
    def weight(self):
        return self.__weight
    
        
    @weight.setter
    def weight(self, value):
        if not isinstance (value,(float, int)):
            raise ValueError("Weight must be a number")
        if not (0 < value <= 120):
            raise ValueError("Age is unrealistic")
        self.__weight = value
        
            
        

patients = [
    Patient(name='Alex', age=30, weight=70),
    Patient(name='Mary', age=22, weight=55),
    Patient(name='John', age=40, weight=90) #'forty'
    ]
for patient in patients:
    sorted_patients = sorted(patients, key=lambda p: p.age)
    print(repr(sorted_patients))