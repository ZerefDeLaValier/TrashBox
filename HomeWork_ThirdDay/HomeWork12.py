#!/usr/bin/python3
c = 1
for i in range(10, 100, 1):
    if (i % 2 != 0) and (i % 13 == 0):
        c *= i
print(c)