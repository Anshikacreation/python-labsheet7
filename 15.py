file = open("data.txt", "r")

content = file.read()
file.close()

old = input("Enter word to replace: ")
new = input("Enter new word: ")

content = content.replace(old, new)

file = open("data.txt", "w")
file.write(content)
file.close()

print("Word replaced successfully.")