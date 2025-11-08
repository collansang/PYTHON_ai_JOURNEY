def check_temp(temp=36.5):
    if temp < 36:
        return 'low temperature'
    elif temp > 38:
        return 'high temperature'
    else:
        return 'normal temperature'
    
def analyze_temp(name, temp = 36.5):
    condition = check_temp(temp)
    return f'{name}, has {condition} of {temp}.'

def avg_temp(temps=[36.5,56.7,38,5]):
    average = sum(temps) / len(temps)
    return round(average, 1)

patients = [
    {'name' : 'Collan', 'temp': 30.4},
    {'name' : 'Volca', 'temp' : 36.5},
    {'name': 'Kibeti', 'temp': 40.1}
]

for p in patients:
    print(analyze_temp(p['name'], p['temp']))

all_temps = [p['temp'] for p in patients]
print(f'average teperature is :{avg_temp(all_temps)}')
    
