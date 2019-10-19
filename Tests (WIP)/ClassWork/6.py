#!/usr/bin/python3
n = [1,0,-1,5,-6]
m = 0
for i in range(len(n)):
    m = m + n[i]
m = m / len(n)
for i in range(len(n)):
    if n[i] > m:
        print(n[i])
