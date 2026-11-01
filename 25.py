import csv

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)

    name = input("Enter student name: ")
    age = input("Enter age: ")
    marks = input("Enter marks: ")

    writer.writerow([name, age, marks])

print("New record added successfully.")