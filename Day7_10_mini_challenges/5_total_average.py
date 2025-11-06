#ask the user to enter numbers
#user should decide how many numbers they want
#ask if they need sum or average
#compute and print the results


count = int(input('How many numbers will you input: '))
numbers = []
for n in range(count):
       while True:
            try:
                num = int(input(f'Enter digit {n+1}: '))
                numbers.append(num)

                break
            except ValueError:
                print('Invalid input. please enter a valid number')
    


op = input('Dou want average (av) or sum (sum) of these numbers: ').strip().lower()
if op == 'sum':
    result = sum(numbers)
    print(f'The sum of these {numbers} is {result}')
elif op == 'av':
    result = sum(numbers) / len(numbers)
    print(f'The evrage of {numbers } is {result:.2f}')

  
