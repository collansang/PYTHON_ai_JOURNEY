#End of Week 2


# Goal: Build a single, readable script that demonstrates:
        # store a list of patient dictionaries,
        # write/read that list to/from a JSON file,
        # inspect and update records via the console, and
        # handle simple input errors and missing/corrupt files gracefully.

import json
import os

DATA_FILE = "patient_db.json"

def check_temp(temp):
    if temp > 37.5:
        return "high temperature"
    elif temp <= 36:
        return "low temperature"
    else:
        return "normal temperature"
    


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
        
    except json.JSONDecodeError:
        print("warning: patients_db.json is corupted, starting a new empty list")
        return[]


def save_data(data):
    with open("patient_db.json", "w") as file:
        json.dump(data, file, indent=2)
 

def add_patient(data):
                try:
                                      
                    name = input("enter the name: ").strip()
                    temp = float(input("enter temperature: "))
                    age = int(input("enter the age: "))
                    symptoms = input("Enter symptoms (comma separated): ")
                    symptoms_list = [s.strip() for s in symptoms.split(",") if s.strip()]                  
                
                except ValueError:
                     print("Invalid input. Patient not recorded")
                    
                patient = {
                        "name" : name,
                        "age" : age,
                        "temperature" : temp,
                        "status" : check_temp(temp),
                        "symptoms" : symptoms_list        
                        }    
                        
                data.append(patient)
                save_data(data)
                print("patient successfully recorded")


def view_patient(data):
    if not data:
          print("No patients found\n")
          return
    
    for p in data:
         print(f"{p['name']} - {p['age']} - {p['temperature']}℃ {p['status']}")
    print()


def search_patient(data):
     name = input("enter name to search: ").strip().lower()
     results = [p for p in data if p["name"].lower().strip() == name]

     if not results:
          print("No patient found\n")
          return 
     p = results[0]
     print(f"\nName:  {p['name']}")
     print(f"\nage:  {p['age']}")
     print(f"\ntemperature:  {p['temperature']}")
     print(f"\nstatus:  {p['status']}")
     print(f"\nsymptoms:  {', '.join(p['symptoms'])}")

def update_temperature(data):
     name = input("enter the patient name to update: ").strip().lower()

     for p in data:
          if p["name"].lower() == name:
               try:
                    
                new_temp = float(input("enter the the new temperature: "))
               except ValueError:
                    print("invalid temperature")
                    return
               
               p["temperature"] = new_temp
               p["status"] = check_temp(new_temp)
               save_data(data)
               print("Temperature updated successfully.\n")
               return
          
     print("Patient not found")

def menu():
     data = load_data()
     while True:
          print("===========================PATIENT MANAGER======================")
          print("1. Add patient")
          print("2. View all patients")
          print("3.Search a patient")
          print("4. Update a patient")
          print("5. Exit/Quit")
          print("===========================PATIENT MANAGER======================")
          

          choice = input("Choose option:").strip()

          if choice == "1":
               add_patient(data)
          elif choice == "2":
              view_patient(data)
          elif choice == "3":
              search_patient(data)
          elif choice == "4":
              update_temperature(data)
          elif choice == "5":
               break
          else:
               print("Invalid choice")
               

menu()


          