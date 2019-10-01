#!/usr/bin/python3
n = int(input())
c = 1
for i in range(1, n, 1):
    c *= i
c = c * n
print(c)