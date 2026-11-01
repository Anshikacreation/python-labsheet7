file = open("data.txt", "r")

lines = file.readlines()

longest = max(lines, key=len)

print("Longest line:", longest)

file.close()