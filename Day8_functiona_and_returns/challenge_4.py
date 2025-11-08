#PATIENT SUMMARY

# Create a list of patients (with names + temps)
# Use your functions to:
  # Print each patient’s name + diagnosis
  # Display the average temperature of the group

def analyze_patient(name, temp):
    if temp < 36:
        condition = 'low temperature'
    elif temp > 40:
        condition =  'fever'
    else:
        condition =  'normal temperature'
    return f'{name} has {condition} of {temp}'

def avg_temp(temps):
    average = sum(temps) / len(temps)
    return round(average, 1)


patients = [
    {'name' : 'Collan', 'temp' : 37.5},
    {'name' : 'Major', 'temp' : 36},
    {'name' : 'Collins', 'temp' : 38},
    {'name' : 'Kibet', 'temp' : 39}
]

for patient in patients:
    name = patient['name']
    temp = patient['temp']
    print(analyze_patient(name, temp))

all_temp = [p['temp'] for p in patients]# The next code is the long version of this for understanding.

# all_temp = []
# for p in patients:
#     all_temp.append('temp')

print(f'Average temperature is {avg_temp(all_temp)} ℃')
    

