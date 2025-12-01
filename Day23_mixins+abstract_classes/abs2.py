# If the abstract class appears BEFORE the mixin that provides the implementation, the abstract method remains unimplemented.

from abc import ABC, abstractmethod
class A(ABC):
    @abstractmethod
    def to_dict(self):
        pass
class RunMixin:
    def to_dict(self):
        return "Show up the most when you feel like quitting/notshowing up at all"

class C(RunMixin, A):#here A is after RunMixin, if interchanged it will give an error.
    pass