import csv

with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Age", "Marks"])

    writer.writerow(["Anshika", 21, 90])
    writer.writerow(["Rahul", 22, 85])
    writer.writerow(["Priya", 20, 95])

print("CSV file created successfully.")