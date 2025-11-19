#Using getter and setter methods
#getter gets the access to private data
#setter modifies private data

#a class derived from another class can access protected data 

class Students:
    def __init__(self, name, age, adm):
        self.name = name#public instance
        self._age = age # protected
        self.__adm = adm #private
    
    def get_adm(self):# an example of a getter, later we will use it to access adm if we want to. This is a safer and prefered method
        return self.__adm
    
    def set_adm(self, x):#Setter. we will use this to modify our data
        #you can also add logics here if you want to
        if x >20000:
            print( "adm invalid")
        else:
            self.__adm = x   
        
        
#     def __display(self):#getter 
#         print(f"Hi {self.name} your adm is {self.__adm} and you are {self._age} years old")   
    
#     def displayStudents(self):
#         self.__display()
        
        
# class Branch(Students):
#     def show(self):
#         print(f"you are {self._age} years old")


stu1= Students("Collan", 21,18233)
stu1= Students("Eric", 22,19865)

# print(stu1.show())

print(stu1.get_adm())#ith help of getter we accessed adm
stu1.set_adm(23452)#with the help of a setter wevw modified adm to 24
print(stu1.get_adm())#we use get to access updated info



#BUT NOW THIS METHOD IS OUTDATATED AND THERE IS A BETTER WAY TO DEAL WITH ENCAPSULATIONS @property check property file