# RULE 1 — A class is abstract if ANY abstract method/property remains unimplemented

from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def one(self):
        pass
    
    @abstractmethod
    def two(self):
        pass
class B(A):
    def one(self):
        print("one implemented")

b = B()  # This will raise TypeError: Can't instantiate abstract class B with abstract methods two    