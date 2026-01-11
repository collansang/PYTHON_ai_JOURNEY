import json
class Patient:
    def __init__(self,patient_id, name, age ):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        
    def to_dict(self):
        return{
            "patient_id" : self.patient_id,
            "name" : self.name,
            "age" : self.age
        }
        
    @classmethod
    def from_dict(cls, data):
        return cls(#cls = clas Patient
                   #data = dictionary
            patient_id = data["patient_id"],
            name = data["name"],
            age = data["age"]
        )


p1 = Patient(1, "Collo", 21)#this is an object of class Patient, JSON does not suppoer object serialization, so we have to convert to a dictionary first. done above in def to_dict
p2 = Patient(2, "Moses", 22)

#after converting to to dictionary, we serialize it, then  to json
#to load back to object we deserialize  from json to dictionary then from dictionary  to object as above def from_dict

data = p1.to_dict()

with open("patients.json", "w") as file:
    json.dump(data, file) #serializing to json file

with open("patients.json", "r") as file:
    data = json.load(file)
p1 = Patient.from_dict(data) #deserializing from json file to dictionary then to object