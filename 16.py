file = open("data.txt", "r")

lines = file.readlines()

if lines:
    print("First line:", lines[0])
    print("Last line:", lines[-1])
else:
    print("File is empty.")

file.close()