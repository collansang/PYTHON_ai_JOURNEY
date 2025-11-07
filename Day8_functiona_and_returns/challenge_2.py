#PATIENT ANALYZER

# Write a function analyze_patient(name, temp) that:
# Uses your check_temp() from Challenge 1
# Returns a string message like
# "Collan has a fever of 38.2°C" or
# "Diana’s temperature is normal."

def temperature(value):
    if value > 37.5:
        return'fever'
    elif value >= 36:
        return 'normal'
    else:
        return 'low temperature'
 
def analyze_temp(name, temp):
    condition = temperature(temp)#here temp relates to value
    return f'{name } has a {condition} of {temp}'

print(analyze_temp('Collan', 36))
print(analyze_temp('Collan', 37))
print(analyze_temp('Cjob', 40))