#!/usr/bin/python3
import re
i1 = str(input("1 "))
i1o = re.split(r' ', i1)
space = 0
for i in range(len(i1)):
    if i1[i] == " ":
        space+=1

if space == 1: #2x2
    i2 = str(input("2 "))
    i2o = re.split(r' ', i2)

elif space == 2: #3x3
    i2 = str(input("2 "))
    i2o = re.split(r' ', i2)
    i3 = str(input("3 "))
    i3o = re.split(r' ', i3)
elif space == 3: #4x4
    i2 = str(input("2 "))
    i2o = re.split(r' ', i2)
    i3 = str(input("3 "))
    i3o = re.split(r' ', i3)
    i4 = str(input("4 "))
    i4o = re.split(r' ', i4)



