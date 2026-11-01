import csv

with open("students.csv", "r") as file:
    reader = csv.reader(file)

    data = list(reader)

    rows = len(data) - 1
    columns = len(data[0]) if data else 0

print("Total rows:", rows)
print("Total columns:", columns)