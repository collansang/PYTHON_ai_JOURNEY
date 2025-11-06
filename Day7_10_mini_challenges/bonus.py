# Ask how many patients to add
# For each patient, ask:
    # name
    # temperature
# Store each patient as a dictionary
# Add all patients into a list
# Display everyone’s data neatly
# Check and show who has a fever (temp > 37.5 °C)

patient_num = int(input('How many patients do you wanna record today: '))

patients = []

for pat in range(patient_num):
    while True:
        try:
            name = input(f'Enter patient`s {pat +1} name: ')
            temp = float(input(f'Enter patien`s {pat+1} temperature'))
            if temp < 30 or temp >45:
                print('Temperature should be between 30 and 45')

            else:
                patients.append({'name' : name, 'temperature' : temp})
                
                print('Recoeded successfully')
            
            if temp > 37.5:
                print(f'patient {pat+1} is has fever')
            elif temp <30:
                print(f'patient {pat+1} has low temperatures')
            else:
                print(f'patient {pat+1} has normal temperatures.') 
            print(f'{name} : {temp}')                  
            break
            
        except ValueError:
            print('Invalid inputs try again')

        

print('==========================patients summary===================================')
print(f'Total patients recorded: {len(patients)}')
for p in patients:
    print(f'{p['name']} - {p['temperature']}')