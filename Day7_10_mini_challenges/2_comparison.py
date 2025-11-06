#ask the user to input two numbers
#determine which is greater and print the result
#if equal print the result as well


while True:
    try:
        x = int(input('Enter your first random number or 0 to quit: '))
        if x == 0:
            break
        y = int(input('Enter your second random number or 0 to quit: '))
        if y == 0:
            break
        if x > y:
            print(f'{x} is greater than {y}')
        elif y > x:
            print(f'{y} is greater than {x}')
        else:
            print('They are equal!')
            break
    except ValueError:
        print('Invalid input please try again')



