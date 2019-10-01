#!/usr/bin/python3
percent = 1.03
s = int(input('Sum of your cash?'))
n = int(input('Years for store?'))

for i in range(n):
    s = s * percent
print(s)