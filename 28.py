import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    students = list(reader)

    if students:
        highest = max(students, key=lambda x: float(x["Marks"]))

        print("Student Name:", highest["Name"])
        print("Highest Marks:", highest["Marks"])
    else:
        print("No records found.")