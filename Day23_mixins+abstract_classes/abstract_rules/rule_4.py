# Only the class that fully implements the abstract interface is instantiable


# Below:
        #A- abstract
        #B - abstract (it inherits from A)
        #C- concrete(it implements all abstract methods)
        
    
    
from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def calculate(self):
        pass
    
class B(A):
    pass

class C(B):
    def calculate(self):
        return 321