class Patient:
    def __init__(self, patient_id, name, age):
        self.patient_id = patient_id
        self.name = name
        self.age = age

    def to_dict(self):
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "age": self.age
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            patient_id=data["patient_id"],
            name=data["name"],
            age=int(data["age"])
        )
