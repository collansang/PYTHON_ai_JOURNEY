# If any parent class has already provided a concrete implementation of an abstract method, subclasses DO NOT need to implement it again.

from abc import ABC, abstractmethod

class A(ABC):
    @abstractmethod
    def to_dict(self):
        pass
    
class B(A):
    def to_dict(self):
        return "If you gonna start something, finish it, otherwise dont even start"
class C(B):
    pass

c= C()
print(c.to_dict())
    
    