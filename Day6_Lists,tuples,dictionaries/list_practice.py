#Create a list of 5 ward names. Print the second and last ward.
#Add a ward named "Maternity"
#Remove the first ward
#Create a new list using comprehension (ward-name lengths)
ward_names = ['A', 'B', 'S', 'G', 'K']
print('second word ',ward_names[1])
print('last word:',ward_names[-1])

ward_names.append('martenity')
print(ward_names)

ward_names.pop(0)
print(ward_names)

ward_names_lengths = [len(ward) for ward in ward_names]
print('ward name lengts',ward_names_lengths)