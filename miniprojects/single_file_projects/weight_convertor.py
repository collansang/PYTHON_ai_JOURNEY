try:
    weight = float(input("Enter the weight: "))
    if not (1<weight<250):
        raise ValueError("weight not realistic")
    
    while True:
        unit =  unit = input("Enter the unit of your weight Kgs/Lbs").strip().lower()
        if unit == "kgs":
            weight = round(weight * 2.205, 2)
            print(f"Your weight is {weight} Lbs")
        elif unit == "lbs":
            weight = round(weight/2.205,2)
            print(f"Your weight is {weight} Kgs")
        else:
            print(f"{unit} is Invali unit!!")
        break   
except ValueError as e:
    print("Error!! ",e)    