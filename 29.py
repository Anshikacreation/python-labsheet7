import csv

search_name = input("Enter student name: ")

found = False

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["Name"].lower() == search_name.lower():
            print("Record found:")
            print(row)
            found = True

if not found:
    print("Student not found.")