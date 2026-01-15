class Patient:
    def __init__(self, pid, name, age, weight, height):
        self.pid = pid
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        
    def to_dict(self):
        return{
            "pid":self.pid,
            "name":self.name,
            "age":self.age,
            "weight":self.weight,
            "height":self.height
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["pid"],
            data["name"],
            data["age"],
            data["weight"],
            data["height"]
            
        )