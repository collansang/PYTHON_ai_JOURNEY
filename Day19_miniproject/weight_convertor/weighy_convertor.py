#practicing if statements



try:
    weight = float(input("Enter your weight in kilograms or pounds: "))
        
    if not (1 < weight < 500):
        raise ValueError("weight not realistic")  
    
    
    while True:    
        unit = input("Is your unit in (kilograms)Kgs or (pounds)Lbs: ").lower()    
        if unit == "lbs":
            converted= round(weight / 2.205, 2)
            print(f"Your weight is {converted} Kgs")
            break
           
        elif unit == "kgs":
            converted= round(weight * 2.205, 2)
            print(f"Your weight is {converted} Lbs")
            break
            
        else:
            print(f"{unit} is an invalid input ")
            
        break
        
except ValueError as e:
    print("Error", e)
    