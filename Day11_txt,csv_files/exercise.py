

import os
patients_num = int(input('How many patients do you wish to record:  '))
def patient_check(patients):
    with open('Patient_report.txt', 'w') as file:
        file.write('Patients report summary\n')
        file.write('='*50)
        file.write('\n')#just for spacing purposes
        for p in patients:
            file.write(f"{p['name']} - {p['temp']} - {p['status']}\n")
    print('Recorded successfully')

def check_temp(temp):
    if temp >39:
        return 'hyperthermic'
    elif temp <36:
        return 'hypothermic'
    else:
        return 'normal'
    
patients = []

for p in range(patients_num):
        while True:

            name = input(f'Enter the name of patient {p+1}: ' )
            if not name:
                print('Name cannot be blank')
                continue
            break
        while True:
                try:
                    temp = float(input(f'Enter the temperature of {name}: '))
                    if temp > 30 and temp <50:
                         break
                    else:
                         print('Temperature must be between 30 and 55')
                except ValueError:
                    print('Please enter a valid temperature')

        status = check_temp(temp)
        patients.append({'name' : name, 'temp' : temp, 'status' : status}) 
        print(f'recorded:{name} - {temp} - {status}')
   
patient_check(patients)