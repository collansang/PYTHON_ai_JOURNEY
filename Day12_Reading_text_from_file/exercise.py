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

fever = 0
normal = 0
low = 0



for p in patients:
    if p["temperature"] > 38:
        fever +=1
        p["stat"] = "fever"
        status = "high temperature"  
    elif p["temperature"] <= 36: 
        low +=1  
        p["stat"] = "low"     
        status = "Low temperature"
    else: 
        normal +=1   
        p["stat"] = "normal"   
        status = "normal temperature"
    print(f"{p["name"]} - {p["temperature"]} - {status}")


with open("Summary_report.txt" , "w") as file:
    file.write("    ==============================PATIENTS SUMMARY REPORT====================\n")
    for p in patients:
        file.write(f"{p["name"]} - {p["temperature"]} - {p["stat"]} \n")
    file.write(f"====================================CATEGORY COUNTS======================================\n")
    file.write(f"fever cases: {fever}\n")
    file.write(f"normal cases : {normal}\n")
    file.write(f"Low temperature cases {low}\n")
