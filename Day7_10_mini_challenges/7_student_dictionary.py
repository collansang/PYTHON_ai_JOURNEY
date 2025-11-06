#create a dictionary that stores
 #name, age, weight,grade(A-D)conciousness
#print each key :value

patients = (
    {'name': 'Calvince', 'age' : 24, 'weight' : 57, 'grade' : 'A'},
    {'name' : 'Collan', 'age' : 21, 'weight' : 50, 'grade' : 'A'},
    {'name' : 'Eric', 'age' : 23, 'weight' : 56, 'grade' : 'C'}

)
print('=======================patients age=======================')
for name in patients:
    print(name['name'] ,'-' ,name['age'])
print('=======================patients weight=========================')
for p in patients:
    print(p['name'], '-', p['weight'], 'Kg')
print('==============================patients temerature=================================')
for t in patients:
    print(t['name'], '-', t['grade'])

print('=======================summary===========================')
for s in patients:
    print(s['name'], '-', s['age'], '- ', s['weight'],'-', s['grade'])