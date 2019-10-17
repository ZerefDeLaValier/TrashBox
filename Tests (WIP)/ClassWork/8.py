#!/usr/bin/python3
n = [1,0,-1,5,-6,6,2,4,1,7,4]
m = 0
p = 1
for i in range(len(n)):
    if (n[i]%2 == 0) and (i%2 != 0):
        m += n[i]
        p += 1
m = m / p
print(m)