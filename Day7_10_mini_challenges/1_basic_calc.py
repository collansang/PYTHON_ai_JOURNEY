#ask the user for a starting value, second value, operator
#perform the calculation and print the answer



f_number = float(input('Enter the first number: '))
op = input('Choose the operator(+, -, *, /, //, %): ').strip()
s_number = float(input('Enter the second number: '))

try:
    if op =='+':
        result = f_number + s_number
        
    elif op == '-':
        result = f_number - s_number
    elif op == '*':
        result = f_number * s_number
    elif op == '/':
        result = f_number/s_number
    elif op == '//':
        result = f_number // s_number
    elif op == '%':
        result = f_number % s_number
    elif op == '**':
        result = f_number ** s_number
    else:
            raise ValueError('Invalid operator')
    print(f'The result of {f_number}{op}{s_number} is: {result}')

except ValueError as e:
        print('error', e)

except ZeroDivisionError:
        print('Error. Number cannot be devided by zero')