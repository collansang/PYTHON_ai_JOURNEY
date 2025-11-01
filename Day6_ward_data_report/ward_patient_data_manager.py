#  Ward Patient Data Manager

#ask the clinician how many wards to record
#for each ward ask 1 ward name, 2 number of patients, 3 average patient temperature
#validate each each entry, no -ve patients, temp range 30-45 and reprompt if invalid
#print each wards data, total patients and ward with highest average temp

# Step 1: Create an empty dictionary to store ward data
wards = {}

# Step 2: Ask for number of wards to record
while True:
    try:
        num_wards = int(input("Enter number of wards to record: "))
        if num_wards <= 0:
            raise ValueError("Number of wards must be greater than zero.")
        break
    except ValueError as e:
        print(" Invalid input:", e)
        print("Please enter a valid positive number.\n")

# Step 3: Loop through each ward
for i in range(num_wards):
    print(f"\n--- Ward {i+1} ---")
    
    # Ask for ward name
    ward_name = input("Enter ward name: ").strip()
    
    # Step 4: Get and validate number of patients
    while True:
        try:
            patients = int(input(f"Enter number of patients in Ward {ward_name}: "))
            if patients < 0:
                raise ValueError("Patient count cannot be negative!")
            break
        except ValueError as e:
            print(" Error:", e)
    
    # Step 5: Get and validate average temperature
    while True:
        try:
            avg_temp = float(input(f"Enter average temperature for Ward {ward_name} (°C): "))
            if avg_temp < 30 or avg_temp > 45:
                raise ValueError("Temperature out of realistic range (30–45°C)!")
            break
        except ValueError as e:
            print(" Error:", e)
    
    # Step 6: Store valid data in the dictionary
    wards[ward_name] = {"patients": patients, "avg_temp": avg_temp}

# Step 7: Compute total and hottest ward
total_patients = sum(ward["patients"] for ward in wards.values())
hottest_ward = max(wards, key=lambda w: wards[w]["avg_temp"])

# Step 8: Print summary
print("\n=====  Ward Summary =====")
for name, data in wards.items():
    print(f"Ward {name} → Patients: {data['patients']}, Avg Temp: {data['avg_temp']}°C")

print(f"\nTotal patients: {total_patients}")
print(f"Hottest ward: {hottest_ward} ({wards[hottest_ward]['avg_temp']}°C)")