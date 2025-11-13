# #Exercise 1 — Read All Rows Correctly
import csv
# with open("patients.csv" , "r") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)


#Exercise 2 — Use DictReader

# with open("patients.csv", "r") as file:
#     d_reader = csv.DictReader(file)
#     for row in d_reader:
#         print(row)


#Exercise 4 — Write to a New CSV
try:

    def check_temp(temp):
            if temp >37.5:
                return "fever"
            elif temp <= 36:
                return "low temperature"
            else:
                return "normal temperature"


    with open("patients.csv", "r") as file:
        reader = csv.DictReader(file)
        
        names = ["name", "temperature", "condition"]
        with open("summary.csv", "w", newline="") as out_file:
        
            writer = csv.DictWriter(out_file, fieldnames = names)
            writer.writeheader()
            
            for row in reader:
                name = row["name"]
                try:

                    temperature = float(row["temperature"])
                except ValueError:
                    print(f"skipping data for {row.get('name', 'unknown')} : {row["temperature"]} ")# find more about .get in notes.py
                    continue
                row["condition"] = check_temp(temperature)#added a new row   
                
                filtered_row = {key:row[key] for key in writer.fieldnames}
                writer.writerow(filtered_row)# below os another way to do it
                
                # writer.writerow({
                #     "name" : row["name"],
                #     "temperature" : row["temperature"],
                #     "condition" : row["condition"]
                # }) 
except FileNotFoundError:
    print("file not found")
except PermissionError:
    print("you are not authorised for this access")
except Exception as e:
    print("Error:", e)

