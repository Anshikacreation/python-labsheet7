file = open("data.txt", "a")

text = input("Enter new content: ")
file.write("\n" + text)

file.close()

print("Content appended successfully.")