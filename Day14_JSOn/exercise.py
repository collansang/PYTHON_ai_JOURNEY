# Create a small script that:
        # Stores 3–5 patient dictionaries in a list.
        # Writes them to a file (patients.json).
import json
def check_temp(temp):
    if temp > 37.5:
        return "high temperature"
    elif temp <= 36:
        return "low temperature"
    else:
        return "normal temperature"
    
patients = [
    {"name" : "Collan Sang", "age" : 21, "temperature" : 35.5},
    {"name": "Diana Chebet", "age": 29, "temperature": 38.9},
    {"name": "Grace Mwende", "age": 34, "temperature": 36.7},
    {"name" : "Alfred Wekesa", "age" : 24, "temperature" : 37.0},
    {"name" : "Mark Otieno", "age" : 29, "temperature" : 36.7}
]

with open("patients_1.json", "w") as f:
    json.dump(patients, f, indent=2 )

with open("patients_1.json", "r") as f:
    data = json.load(f)
    
    
    for d in data:
        try:
            temp = float(d["temperature"])
            condition = check_temp(temp)
            print(f"{d["name"]} - {temp} - {condition}")
        except (KeyError, ValueError,TypeError)as e:
            print("skipping an invalid patient record",e)
        

