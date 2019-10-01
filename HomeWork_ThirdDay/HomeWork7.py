#!/usr/bin/python3
pair = 10
numbers = []
out = []
for i in range(pair):
	num = int(input("Num1: "))
	num2 = int(input("Num2: "))
	numbers.append(num)
	numbers.append(num2)
print(numbers)


for i in range(0, len(numbers), 2):
	out.append(max(numbers[i],numbers[i + 1]))
print(out)