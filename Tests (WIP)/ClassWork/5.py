#!/usr/bin/python3
n = [1,0,-1,5,-6]
m = 0
for i in range(len(n)):
    if (n[i] < 0) and (n[i]%2 == 0):
        m = m + n[i]
print(m)