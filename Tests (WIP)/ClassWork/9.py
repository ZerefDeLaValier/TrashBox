#!/usr/bin/python3
n = [1,0,-1,5,-6,6,2,4,1,7,4]
p = 0
for i in range(len(n)):
    if n[i] > 0:
        p += 1
print(p)