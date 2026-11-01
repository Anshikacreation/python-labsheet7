file = open("data.txt", "r")

content = file.read()

word = input("Enter word to search: ")

if word.lower() in content.lower().split():
    print("Word found.")
else:
    print("Word not found.")

file.close()