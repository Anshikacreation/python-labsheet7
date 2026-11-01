file = open("data.txt", "w")

n = int(input("Enter number of lines: "))

for i in range(n):
    line = input("Enter line: ")
    file.write(line + "\n")

file.close()

print("Data saved successfully.")