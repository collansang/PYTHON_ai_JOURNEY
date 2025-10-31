#utensils counter
utensils = ['sufurias', 'plates', 'forks',]
utensil_count = {}
total = 0
print('enter the number of utensils you have below')
for utensil in utensils:
    while True:
        try:
            count = int(input(f'Enter the number of {utensil} you have : '))

            if count <0:
                raise ValueError('utensils cant be negative!')
            break
        except ValueError as x:
            print('please enter a valid number')
    utensil_count[utensil] = count
    total += count
    print()
    for utensil, count in utensil_count.items():
        print(f'{utensil} : {count}')
    print(f'your total number of utensils is: {total}')

    
            

                    
