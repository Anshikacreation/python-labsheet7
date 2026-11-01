file1 = open("data1.txt", "r")
file2 = open("data2.txt", "r")

content1 = file1.read()
content2 = file2.read()

file1.close()
file2.close()

file3 = open("merged.txt", "w")

file3.write(content1 + "\n" + content2)

file3.close()

print("Files merged successfully.")