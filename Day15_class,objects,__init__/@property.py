#property
#you can add logics using this encapsulation

class Patients:
    def __init__(self, name , age, temperature):
        self.name = name
        
        self.__age = None
        self.__temperature = None
        
        self.age = age
        self.temperature = temperature
        
    @property
    def temperature(self):
        return self.__temperature
    @temperature.setter
    def temperature(self, new_temperature):        
        if not isinstance (new_temperature, (int, float)):
            raise ValueError("Temperature must be a number")
        if not (34<= new_temperature <= 42):
            raise ValueError("temperature must be between 34 and 42")
        self.__temperature = float(new_temperature)
        
            
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, new_age):
        if not isinstance (new_age, int):
            raise ValueError("Age must be a number")
        if not(0 <=  new_age < 150):
            raise ValueError("age not realistic")
        self.__age = new_age
        
        
patient1 = Patients("Collan", 21, 37.4)
print("Name: ", patient1.name )
print("Age: ", patient1.age )

print("Temperature: ", patient1.temperature)
patient1.temperature = 36.7
print("Updataed temperature: ", patient1.temperature)
patient1.temperature = 40

