#lets read the patients.txt file

with open("patients.txt", "r") as file:
    data = file.read()
    print(data)


#lemme read line by line
with open("patients.txt", "r") as file:
    data = file.readlines()
    print(data)


#lets clean the text using.strip and split
with open("patients.txt", "r") as file:
    for line in file:
        clean = line.strip()#removes \n and spaces.
        name, temp = clean.split(",")#separates text into parts by a comma
        print(f"name : {name.strip()} || temperature:  {temp.strip()}")



