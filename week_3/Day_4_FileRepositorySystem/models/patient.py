class Patient:
    def __init__(self, pid, name, age):
        self.pid = pid
        self.name = name
        self.age = age
        
    def to_dict(self):
        return{
            "pid" : self.pid,
            "name" : self.name,
            "age" :self.age
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["pid"], data["name"], data["age"]  
        )