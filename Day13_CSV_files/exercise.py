# Write a script that:
    # Reads patients from patients.csv
    # Finds those with temperature > 37.5
    # Prints their names and flags them as “Fever detected”

import csv


def check_temp(temp):
     
    if temp > 37.5:
        return  "fever"
    elif temp <= 36:
        return "Low temperature"
    else:
        return "normal temperature"     

with open("patients.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)


    for row in reader:
        name = row["name"]
        temperature = float(row["temperature"])
        age = int(row["age"])
        condition = check_temp(temperature)
        print(f"{name} - {temperature} - {condition}")


