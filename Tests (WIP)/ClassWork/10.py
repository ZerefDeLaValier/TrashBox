#!/usr/bin/python3
n = [1,0,-1,5,-6,6,2,4,1,7,4]
min = n[0]
min_i = 0
for i in range(len(n)-1):
    for j in range(len(n)-i-1):
        if n[j] > n[j+1]:
            n[j], n[j+1] = n[j+1], n[j]
print(n)