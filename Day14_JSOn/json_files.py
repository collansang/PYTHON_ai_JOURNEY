import json
patients = [
    {"name" : "Collan Sang", "age" : "21", "temperature" : 35.5, "symptoms" : ["cough", "fever", "chest pain"]},
    {"name": "Diana Chebet", "age": 29, "temperature": 38.9, "symptoms": ["fever", "headache"]},
    {"name": "Grace Mwende", "age": 34, "temperature": 36.7, "symptoms": ["weakness", "nausea and vomiting"]}
]

# with open("patients.json", "w") as json_file:
#     json.dump(patients, json_file, indent = 4)


with open("patients.json", "r") as file:
    data = json.load(file)
    print(data)