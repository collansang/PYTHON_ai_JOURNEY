#encapsulation
#wrapping up of data and methods into a single unit
#shield - protects data

class Students:
    def __init__(self, name, age, adm):
        self.name = name#public instance
        self._age = age # protected
        self.__adm = adm #private
    
    def __display(self):#getter 
        print(f"Hi {self.name} your adm is {self.__adm} and you are {self._age} years old")   
    
    def displayStudents(self):
        self.__display() #here we call display within the class and the dsplay calls for private data. this way we access the private data        

stu1= Students("Collan", 21,18233)
stu1= Students("Eric", 22,19865)
print(stu1._Students__adm)#eccessing privvate data
print(stu1.displayStudents())#accessing private data using a function to all another funtion calling a fuction with privat data(def displayStudents call display which call private data from primary function)
print(stu1._Students__display())#this is another way of accessing private data callend mangling


