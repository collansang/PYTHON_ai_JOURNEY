from abc import ABC, abstractmethod

class BasePatient(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        
        self.__age = None
        self.__weight = None
        self.__height = None
        
        self.age = age
        self.weight = weight
        self.height = height
        
        @abstractmethod
        def validatea(self):
            pass
        
        @property
        @abstractmethod
        def risk_score(self):
            pass
        
        def __repr__(self):
            return f"{self.__class__.__name__} (name={self.name}, age = {self.__age})"
        
        def __str__(self):
            return f"{self.name} (}self.__class__.__name__})"
        
        
        
        
        