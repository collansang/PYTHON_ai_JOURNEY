#here we`ll break down long codes to small ones for easier redability and fast typying`

#summary 1


patients = [
    {'name': 'Collan', 'temp': 38.2},
    {'name': 'Diana', 'temp': 36.7},
    {'name': 'Faith', 'temp': 35.5},
    {'name': 'Grace', 'temp': 37.9}
]


#Instead of 

all_temps = []
for p in patients:
    all_temps.append(p['temp'])
print(all_temps)

#just write this

all_temps = [p['temp'] for p in patients]
print(all_temps)

# summary on how to print fever patients
fever_patients = [p['name'] for p in patients if p['temp'] >37.5]
print(fever_patients)