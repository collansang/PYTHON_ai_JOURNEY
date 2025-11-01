#calculator for tatal people
wards = ['ward A', 'ward B', 'ward C']
ward_data = {}#empty dictionary that stores key:value (Ward A : 12)
total = 0#initializes counter variable to accumulate the sum of all patients.
print('Enter patients count for each ward')
for ward in wards:
    
    while True:#creates a loop that repeats until we break out. until you give a valid integer
        try:
            patient = int(input(f'Enter the number of patients in ward {ward} '))
            if patient <0:
                raise ValueError('Patiets cannot be a negative value')
            break
        except ValueError:#applies if you type a value that cant be converted to integer eg ten intesd of 10, youll be repromted 
            print('Invalid input! Please try again: ')
    ward_data[ward] = patient#updates an entry in the dictionary
    total += patient#Adds current ward value to the running total (total = total +patient)

print('-------ward summary--------')
for ward,count in ward_data.items():#in ward-data we have (Ward A : 10; Ward B; 12: ward ,recieves a key (Ward A) and count recieves the value (10) in ward_data
    print(f'{ward} : {count} patients')#will print ward and total count per word
print(f'total number of patients are: {total}')#will print total number of patients
    
