#ask the clinician to enter temp of several patients
#for each print diagnosis:
 #hypothermia <35
 #normal 35 - 37.5
 #fever 37.6 - 39
 #high fever >=39

temperature = []
patients = int(input('How many patients do you wanna input?: '))
for x in range(patients):
    while True:
        try:            
            temp = float(input(f'Enter the temperature for patient {x+1}: '))
            
            if temp == 0:
                print('Goood bye')
                exit

            if temp <30 or temp > 50:
                print('Temperature should be betw 30 and 50')
            else:
                temperature.append(temp)
                print('Recorded successfully')
                

            if temp < 35:
                print(f'Patient {x+1} is hypothermic')
                print('Help immediately!')
            elif temp > 35 and temp < 37.5:
                print(f'Temperature normal for patient {x+1}, Keep confirming.')
            elif temp > 38:
                print(f'Patient {x+1} has fever attend to them.')
            else:
                print(f'Patient{x+1} Has very high fever. They need immediate attention')
            print('=' * 40)
            break

        except ValueError:
            print('invalid. Please enter a valid number.')




if temperature:
    print('-----------------Summary----------------')
    print(f'Total patients recorded: {len(temperature)}')
    print(f'Temperatures: {temperature}')
    print('-----------------Summary----------------')


