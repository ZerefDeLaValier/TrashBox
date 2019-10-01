#!/usr/bin/python3
import re
pos = 0
neg = 0
zero = 0
n = str(input())
n1 = re.split(r' ', n)
for i in range(len(n1)):
    if int(n1[i]) < 0:
        neg += 1
    if int(n1[i]) > 0:
        pos += 1
    if int(n1[i]) == 0:
        zero += 1
print('Отрицательные:', neg, ' Положительные:', pos, ' Нули:', zero)
