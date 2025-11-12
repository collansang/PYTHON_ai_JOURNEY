#wrtting into a csv file
import csv

patients = [
    {"name" : "Collan Sang","temperature" : 38.6, "age" : 21 },
    {"name": "Grace Mwende", "temperature": 38.1, "age": 29},
    {"name": "Diana Chebet", "temperature": 37.2, "age": 21},
]

with open("patients1.csv", "w") as csv_file:
    names = ["name", "temperature", "age"]
    writer = csv.DictWriter(csv_file, fieldnames= names)
    writer.writeheader()
    writer.writerows(patients)