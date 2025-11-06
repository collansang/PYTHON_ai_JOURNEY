#store 3 patients ina dictionaty
#name and temperature and determine who has fever

patients = [
    {'name' : 'Norman', 'temp' : 37.5},
    {'name' : 'Morgan' , 'temp' : 38.5},
    {'name' : 'Mary', 'temp' : 34.5},
   
]
for p in patients:
    temp = p['temp']
    if temp > 37.5:
        print(p['name'], 'is hyperthermic')
    elif temp  < 36:
        print(p['name'], 'is hypothermic')
    else:
        print(p['name'], 'has normal temperature.')