try:
    temp = float(input("Enter the temperature: "))
    if not (34< temp< 47):
        raise ValueError ("Temperature should be between 34 and 47")
    
    while True:
        unit = input("Enter the unit (c for ℃ / f for ℉): ").strip().lower()
        
        if unit == "c":
            temp = round(((9 * temp ) / 5)+ 32,2)
            print(f"Your temperature {temp} ℉")
        elif unit == "f":
            temp = round((temp-32) * 5/9, 2)
            print(f"Your temperature {temp} ℃")
        else:
            print(f"{unit} is Invalid unit ")
        break

except ValueError as e:
    print(f"Error!!", e)