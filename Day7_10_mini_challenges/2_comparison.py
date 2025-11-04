#ask the user to input two numbers
#determine which is greater and print the result
#if equal print the result as well

x = int(input('Enter your first random number: '))
y = int(input('Enter your second random number: '))

if x > y:
    print(f'The first number {x} is greater than second number {y}')
elif y > x:
    print(f'The seconf number {y} is greater than first number {x}')
else:
    print('They are both equal')