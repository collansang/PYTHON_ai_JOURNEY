#combining conditionals
temperature = int(input('Enter the temp in degrees celcious: '))
rain = input('Is it raining?: ').lower()

if temperature >30 and not rain == 'yes': # same as if temperature >30 and rain == 'no
    print('Its hot out there. Maybe perfect for swimming, beach.')
elif temperature >=20 and temperature <=30 and rain == 'no':
    print('Perfect weather for working, training, etc.')
elif temperature <20 and rain == 'yes':
    print('Its cold out there, Wear a sweater and take your umbrella')
elif temperature <20 and rain == 'no':
    print('Its cold but not raining, Just wear your sweater')
else:
    print('The weather is unpredictsble, check in th forecast.')