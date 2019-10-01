#!/usr/bin/python3
c = 0
for i in range(51):
    if (i % 5 == 0) or (i % 7 == 0):
        c += i
print(c)