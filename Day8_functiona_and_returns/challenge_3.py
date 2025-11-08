# Create a function average_temp(temps) that:

 # Accepts a list of temperatures (e.g. [36.5, 37.8, 38.0, 36.9])
 # Calculates the average temperature
 # Returns the result rounded to one decimal place

def avg_temp(*temps):
    average = sum(temps) / len(temps)
    return round(average, 1)


print('average temperature')
print(avg_temp(46, 46, 36.7, 34))
