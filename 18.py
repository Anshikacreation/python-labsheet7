file = open("data.txt", "r")

words = file.read().split()
file.close()

unique_words = sorted(set(words))

file = open("unique.txt", "w")

for word in unique_words:
    file.write(word + "\n")

file.close()

print("Unique words saved.")