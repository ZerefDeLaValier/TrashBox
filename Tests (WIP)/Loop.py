#!/usr/bin/python3
numbers = ["0","1","2","3","4","5","6","7","8","9"]
j = 0
n = str(input("Write a string: "))
for i in range(len(n)):
    if n[i] in numbers: 
        continue
    else:
        print(n[i])
