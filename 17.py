file = open("data.txt", "r")

lines = file.readlines()
file.close()

file = open("data.txt", "w")

for line in lines:
    if line.strip():
        file.write(line)

file.close()

print("Blank lines removed.")