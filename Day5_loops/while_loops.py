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


# patients = ['Collan Sang', 'Diana Chebet']# 'Faith Achieng']
# times = ['Morning', 'Afternoon', 'Evening']
# for patient in patients:
#     temp = float(input(f'Plese input {patient}`s temperature: '))
#     while True:
#         time_temp = input(f'Please input time of measurement(Morning/evening/afternoon): ').capitalize()
#         if time_temp in times:
#             break
#         else:
#             print('Invalid time entered. Please try again.')
#     print(f'Recorded temp at the  {time_temp} is {temp} C')

print()

utensils = ['sufurias', 'plates', 'spoons', 'jikos', 'knives']
for utensil in utensils:
    collected = input(f'Have you assembeled the {utensil}? (yes,no): ').lower()
    while collected not in ['yes', 'no']:
        print('Invalid input. Please answer with "yes", or "no".')
        collected = input(f'Have you assembeled the {utensil}? (yes,no): ').lower()
    if collected == 'yes':
        print(f'{utensil} assembelede')
    else:
        print(f'Please assemble the {utensil} as soon as possible.')
    print('Search ended.')
