#if/elif/else statements
age = int(input('How old are you?'))

if age >= 18:
    print('You are an adult')
else:
    print('You are a child')


num = int(input('Enter any number:'))
if num > 0:
    print('You entered a positive number')
elif num == 0:
    print('You entered a Zero.')
elif num < 0:
    print('You entered a negative number')
else:
    print('Invalid number')

#ternary operations
age = int(input('Enter your age:'))

message = 'Eligible' if age >=18 else 'Not Eligible'
print(message)