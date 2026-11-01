import csv

with open("students.csv", "r") as source:
    reader = csv.reader(source)
    data = list(reader)

with open("copy.csv", "w", newline="") as destination:
    writer = csv.writer(destination)
    writer.writerows(data)

print("CSV file copied successfully.")