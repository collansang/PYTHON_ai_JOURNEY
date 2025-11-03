#tuples
#ordered and immutable

patient_tuple = ('Faith', 21, 36.8)
name = patient_tuple
# print(name)
identity = ('name', 'age', 'temp')
for identit, name in zip(identity, patient_tuple):
    print(f'{identit}: {name}')