file = open("data.txt", "r")

content = file.read()

lines = content.splitlines()
characters = len(content)

print("Total lines:", len(lines))
print("Total characters:", characters)

file.close()