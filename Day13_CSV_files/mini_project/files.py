#write a code that:
        #wtites summary on a diffrent csv file
               # add a condition whether fever, normal or high temp 
        #creates a new csv file and stores bad data for later review

import csv

def check_temp(temp):
    if temp > 37.5:
        return "high temperature"
    elif temp <= 36:
        return "low temperature"
    else:
        return " normal temperature"
    
try: 
    with open("patients.csv", "r") as infile, \
        open("summary.csv", "w",newline= "") as outfile, \
        open("errors.csv", "w", newline = "") as errorfile:
        
        reader = csv.DictReader(infile)
        names = ["name", "temperature" , "condition"]
        writer = csv.DictWriter(outfile, fieldnames = names)
        writer.writeheader()

        error_names = reader.fieldnames + ["error_reason"]
        error_writer = csv.DictWriter(errorfile, fieldnames = error_names)
        error_writer.writeheader()


        for row in reader:
            try:
                temperature = float(row["temperature"])
            except ValueError:
                row["error_reason"] = "invalid_temperature"
                error_writer.writerow(row)
                print(f"logged bad data for {row.get('name', 'unknown')}")
                continue

            row["condition"] = check_temp(temperature)
            update = {key:row[key] for key in writer.fieldnames }
            writer.writerow(update)

except FileNotFoundError:
    print("File does not exist")
except PermissionError:
    print("you are not authorised to do so")
except Exception as e:
    print("Error!", e)
