# An abstract @property requires at least the getter to be implemented
#python treats abstract properties diffrently 
    #the getter is mandatory to implement
    #setter is optional unless explicitly abstract
    
#In example below: 
 #                  setter exist, getter is missing
                  # will print type error
                  
                  
from abc import ABC, abstractmethod
class A(ABC):
    @property
    @abstractmethod
    def x(self):
        pass

class B(A):
    @x.setter
    # @property
    
    def x(self, value):
        print(f"Setting x to {value}")
        
c = B()