#!/usr/bin/python3
n = [1,0,-1,5,-6]
min = n[0]
max = n[0]
for i in range(1,len(n)):
    if n[i] < min:
        min = n[i]
    if n[i] > max:
        max = n[i]
print(max, min, max - min)
    