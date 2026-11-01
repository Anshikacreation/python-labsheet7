file = open("data.txt", "r")

content = file.read()

word = input("Enter word: ")

count = content.lower().split().count(word.lower())

print("Word occurrence:", count)

file.close()