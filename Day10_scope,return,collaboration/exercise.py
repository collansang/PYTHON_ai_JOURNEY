# make a function that:
  # Asks the user for temperature readings (3 times).
  # Calculates the average using return.
  # Then outside the function, print whether the average is “Normal”, “Fever”, or “Hypothermia”.

temp_list = []
for i in range(3):
    t = float(input(f'Enter the teemperature of patient {i+1}: '))
    temp_list.append(t)


def avg_temp(temps):
    avg = sum(temps) / len(temps)
    return round(avg, 1)


average = avg_temp(temp_list)

print(f'Average temperature = {average}')

if average > 38:
    print(f'Patients are hyperthermic')
elif average < 36:
    print(f'Patients are hypothermic')

else:
    print(f'Patients have normal temperature')


