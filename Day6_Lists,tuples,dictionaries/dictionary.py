# #dictionaries  no duplicates, mutable/changable
# #collection of key.value pairs
# #curly braces, separated by colon

# patient = {
#     'name' : 'Josphin Nakhumicha',
#     'age' : 19,
#     'temp' : 36.7,
#     'ward' : 'C'
# }
# # print(patient)
# #print(patient['name'])# accessing. make sure to use square brackets
# #print(patient.get('bp'))# use .get to find a value, if absent it printds none
# # print(patient.pop('age')) # remove and return value
# print(patient.popitem())# remove last inserted (key, value)
# for name in patient:
#     print(name)


#data for several. its better to use a list of dicts ({})
#dont forget to separate with commas
patients = [
    {'name' : 'Collan', 'age' : 21, 'ward' : 'A1', 'temp' : 36.2},
    {'name' : 'Eric', 'age' : 22, 'ward' : 'B2', 'temp' : 36.6},
    {'name' : 'Calvo', 'age' : 23, 'ward' : 'C3', 'temp' : 37.2},
]
print(patients)

for patient in patients:
    print(patient['name'], '-', patient['age'])
