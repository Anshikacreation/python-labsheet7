file = open("data.txt", "r")

content = file.read()

print(content.upper())

file.close()