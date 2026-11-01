source = open("data.txt", "r")
destination = open("copy.txt", "w")

content = source.read()
destination.write(content)

source.close()
destination.close()

print("File copied successfully.")