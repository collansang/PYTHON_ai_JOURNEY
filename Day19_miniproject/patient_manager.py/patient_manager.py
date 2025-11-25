#design a patient managerthat:
    #Displays list of patients
    #add patients
    #update patients
    #remove a patients
    #design main body function
    
#what i need:
            #patients list
            #

class Patients:
    count = 0
    register = []
    def __init__(self, pid,name, age, temperature, weight, height):
        self.name = name
        self.id = pid
        
        
        self.__age = None
        self.__temperature = None
        self.__weight = None
        self.__height = None
        
        self.age = age
        self.temperature= temperature
        self.weight = weight
        self.height = height
        
        self.patients = []
        Patients.count += 1
        Patients.register.append(self)
        
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if not isinstance (value, int):
            raise ValueError("Age must be a number")
        if not (1< value < 125):
            raise ValueError("That is not a realistic age")
        self.__age = value
        
        
    @property
    def temperature(self):
        return self.__temperature
    
    @temperature.setter
    def temperature(self, value):
        if not isinstance (value, (float, int)):
            raise ValueError("Temperature must be a number")
        if not (34< value < 45):
            raise ValueError("temperature should be between 34 and 45")
        
        self.__temperature = value
    
    @property
    def weight(self):
        return self.__weight
    
    @weight.setter
    def weight(self, value):
        if not isinstance (value, (float, int)):
            raise ValueError("weight must be a number")
        if not (0.5< value < 550):
            raise ValueError("weight should be between 0.5 and 550")
        
        self.__weight = value 
        
        
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        if not isinstance (value, (float, int)):
            raise ValueError("height must be a number")
        if not (0.5< value < 2):
            raise ValueError("height should be between 0.5 and 2")
        
        self.__height = value    


    def display_patients(self):
        for p in self.patients:
            print(p.id, p.name, p.age)
        

        
    def check_temp(self):
        for p in self.patients:
            if p.temperature <= 36:
                status = "low temperature"
            elif p.temperature > 37.5:
                status =  "high temperature"
            else:
                status =  "normal temperature"
            
                
            
       
        

    def add_patients(self):
        pass


    def update_patients(self):
        pass

    def search_patient(self):
        pass
    

    def remove_patients(self):
        pass





        
    