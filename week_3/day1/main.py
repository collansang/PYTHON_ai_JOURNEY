import csv
patients = []
#DESERIALIZATION = Deserialization is the controlled reconstruction of full Python objects from serialized data, restoring structure, type, and behavior that JSON cannot store.
class Patient:#class(blueprint)
    def __init__(self, name, age, weight,height):
        self.name = name
        self.age = age 
        self.weight = weight
        self.height = height
        
    def calculate_bmi(self):
        return round(self.weight/ (self.height **2),2)
    
patients = [
    Patient("Collo", 21, 50, 1.4),
    Patient("Moses", 22, 57, 1.5),
    Patient ("Enock", 32, 64, 1.6)
] 

"""READING CSV"""
with open("patients.csv", "r", newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        p = Patient(
            row["name"],
            int(row["age"]),
            float(row["weight"]),
            float(row["height"])
        )
        patients.append(p)
    for p in patients:
        print(p.name, p.age)
        

"""WRITTING OBJECTS BACK TO CSV"""
with open("output.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["name", "age", "weight", "height", "bmi"])
    for p in patients:
        writer.writerow([
            p.name,
            p.age,
            p.weight,
            p.height,
            round(p.calculate_bmi(), 2)
            
        ])

       


