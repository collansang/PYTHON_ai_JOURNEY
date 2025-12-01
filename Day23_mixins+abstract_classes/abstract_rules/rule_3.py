# Implementing only a setter NEVER overrides an abstract getter

from abc import ABC, abstractmethod
class A(ABC):
    @property
    @abstractmethod
    def value(self):
        pass
    #This does NOT override the abstract property:
    #Because overriding the setter doesn’t create a getter.
class B(A):
    @value.setter
    def value(self, v):
        self._v = v
    