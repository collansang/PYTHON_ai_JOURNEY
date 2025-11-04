#logical test
#prompt the user three numbers
#all should be even numbers and positive
#print the result to the user if correct, and try agin if wrong

while True:
    try:
        num1 = int(input('Enter the fist number: '))
        num2 = int(input('Enter the second number: '))
        num3 = int(input('Enter the third number: '))

        if num1 >0 and num2 > 0 and num3 > 0:
            if num1 % 2 == 0 and num2 % 2 == 0 and num3 % 2 == 0:
                print('Congradulations all numbers are positive and even.')
                break
            else:
                print('All numbers must be even. Try again: ')
        else:
            print('Ell numbers must be positive. Please try again')
    except ValueError:
        print('Invalid input please enter integer values only:')
