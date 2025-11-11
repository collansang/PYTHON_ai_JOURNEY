# #lets read the patients.txt file

# with open("patients.txt", "r") as file:
#     data = file.read()
#     print(data)


# #lemme read line by line
# with open("patients.txt", "r") as file:
#     data = file.readlines()
#     print(data)


# #lets clean the text using.strip and split
# with open("patients.txt", "r") as file:
#     for line in file:
#         clean = line.strip()#removes \n and spaces.
#         name, temp = clean.split(",")#separates text into parts by a comma
#         print(f"name : {name.strip()} || temperature:  {temp.strip()}")



patients  = []
try:

    with open("patients.txt", "r") as file:
        for line in file:
            name, temp = line.strip().split(",")
            patients.append({"name": name.strip(), "temperature": float(temp.strip())})
except FileNotFoundError:
    print("Error: The file you are trying to find does not exist")
except ValueError:
    print("Line incorrectly formated")
total = sum([p["temperature"] for p in patients])
average = total / len(patients)

print(f"Average temperature: {average:.2f} ℃")

for p in patients:
    if p["temperature"] > 38:
        status = "high temperature"  
    elif p["temperature"] <= 36:        
        status = "Low temperature"
    else:       
        status = "normal temperature"
    print(f"{p["name"]} - {p["temperature"]} - {(status)}")
for s in status:

    if status == "high temperature":
        print(f"Patients with high temperature : {len(s)}")
    elif status == "low temperature":
        print(f"Patients with low temperature: {len(s)}")
    else:
        print(f"Patients with normal temeratures {len(s)}")




print("-" * 100)
print("PATIENTS SUMMARY")
print(f"Total patients : {len(patients)}")


# print(f"Patients with {status}:  {sat}")

#print(f"Total patients summary{(num)}")

