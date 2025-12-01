
principle = 0
rate = 0
time = 0

while True:
    principle = float(input("enter the principle amount: "))
    if principle <0:
        print("Principle cannot be below zero")
    else:
        break
    
    
while True:
    rate = float(input("enter the interest rate: "))
    if rate <0:
        print("rate cannot be below zero")
    else:
        break
    
while True:
    time = float(input("Enter time in years; "))
    if time <0:
        print("time cannot be below zero")
    else:
        break


total = principle * pow(1 + (rate/100), time)
print(f"Total amount: Ksh{total:.2f}")