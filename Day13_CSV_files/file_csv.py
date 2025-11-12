
import csv
#comma separated values
#in each line each value is separated with a comma

#reading the csv file
with open("patients.csv", "r") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)


#its better if we treat each row as a dictionary
#we use csv.dictreader

with open("patients.csv", "r") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        print(f"{row["name"]} - {row["temperature"]}℃")
