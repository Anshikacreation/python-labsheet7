file = open("data.txt", "r")

numbers = list(map(float, file.read().split()))

total = sum(numbers)
average = total / len(numbers)

print("Sum:", total)
print("Average:", average)

file.close()