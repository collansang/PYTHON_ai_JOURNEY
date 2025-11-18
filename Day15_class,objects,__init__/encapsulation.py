#encapsulation
#wrapping up of data and methods into a single unit
#shield - protects data

class Students:
    def __init__(self, name, age, adm):
        self.name = name#public instance
        self._age = age # protected
        self.__adm = adm #private
    
    def __display(self):
        print(f"Hi {self.name} your adm is {self.__adm} and you are {self._age} years old")   
    
    def displayPrivateData(self):
        self.__display()         