#Temperature Checker

# Create a function called check_temp(temp) that:
  # Takes a temperature (float)
  # Returns "Fever" if above 37.5
  # Returns "Normal" if between 36 and 37.5
  # Returns "Low" if below 36
# Then call it for different temperatures.

def check_temp(temp):
    if temp > 37.5:
        return 'normal'
    elif temp >= 36:
        return ' normal'
    else:
        return 'hypothermic'
    

print(check_temp(35))
print(check_temp(40))
print(check_temp(37))
