class Patient:
    def __init__(self, name : str, age : int):
        self.name = name
        self.age = age
        
    def to_dict(self):#exports an object to dictionary
        return {
            "name" : self.name,
             "age" : self.age
        }
        
    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            name = data["name"],
            age = data["age"]
        )
        

