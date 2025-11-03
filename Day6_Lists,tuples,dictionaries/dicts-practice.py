#build a small console-based patients manager
# Features
# 1 add patient
# 2 Store each patient as a dictionary
# 3 Keep all in a list
# 4 Display them
# 5 Check who has a fever

patients = []
num_patients = int(input('How many patients do you want to enter?: '))
total = 0

#1
for num in range(num_patients):#will ask the following quizes 3 times. collecting data for three 
    print(f'--------------ENTER THE PATIENTS DETALIS BELOW{num+1}------------------')
    name = input('Name: ')
    age = int(input('Age: '))
    temp = float(input('temperature ℃: '))
    patient = {'name' : name, 'age' : age, 'temp' : temp}
    patients.append(patient)

print('--------------ALL PATIENTS----------------')
for p in patients:
    print(f"{p['name']}, - Age : {p['age']}, Temp : {p['temp']}")


for p in patients:
    total = total + p['temp']
everage = total / len(patients)
print('--------------AVERAGE TEMPERATURE-----------------')
print(f'everage: {everage:.2f} ℃')