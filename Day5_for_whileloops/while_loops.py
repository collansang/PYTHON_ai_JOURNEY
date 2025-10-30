#while loops

# password = ''
# while password != 'Sucre123':
#     password = input('' \
#     'Please reenter your password: ')

# print('Login successfull')


# patients = ['Collan Sang', 'Diana Chebet', 'Faith Achieng', 'Grace Mwende', 'Hellen Aoko', 'Irene Adhiambo']
# time = ['Morning', 'Afternoon', 'Evening']
# for patient in patients:
#     print(f'Patient: {patient}')
#     for tim in time:
#         print(f'{tim} temperature recorded.')
#     print()


patients = ['Collan Sang', 'Diana Chebet', 'Faith Achieng']
times = ['Morning', 'Afternoon', 'Evening']
for patient in patients:
    temp = float(input(f'Plese input {patient} temperature: '))
    while True:
        time_temp = input(f'Please input time of measurement(Morning/evening/afternoon): ').capitalize()
        if time_temp in times:
            break
        else:
            print('Invalid time entered. Please try again.')
    print(f'Recorded temp at the  {time_temp} is {temp} C')