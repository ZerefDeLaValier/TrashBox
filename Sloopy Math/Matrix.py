#!/usr/bin/python3
#import start
import re
def matrix():
    i1 = str(input("First str: "))
    i1o = re.split(r' ', i1)
    space = 0
    for i in range(len(i1)):
        if i1[i] == " ":
            space+=1

    if space == 1: #2x2
        i2 = str(input("Second str: "))
        i2o = re.split(r' ', i2)
        for z in range(2):
            i1o[z] = int(i1o[z])
            i2o[z] = int(i2o[z])

    elif space == 2: #3x3
        i2 = str(input("Second str: "))
        i2o = re.split(r' ', i2)
        i3 = str(input("Third str "))
        i3o = re.split(r' ', i3)
        for z in range(3):
            i1o[z] = int(i1o[z])
            i2o[z] = int(i2o[z])
            i3o[z] = int(i3o[z])
    elif space == 3: #4x4
        i2 = str(input("Second str: "))
        i2o = re.split(r' ', i2)
        i3 = str(input("Third str: "))
        i3o = re.split(r' ', i3)
        i4 = str(input("Fourth str: "))
        i4o = re.split(r' ', i4)
        for z in range(4):
            i1o[z] = int(i1o[z])
            i2o[z] = int(i2o[z])
            i3o[z] = int(i3o[z])
            i4o[z] = int(i4o[z])
    #import end

    #main start
    if space == 1:
        answer = ((i1o[0])*(i2o[1]))-((i1o[1])*(i2o[0]))
        
        
    if space == 2:
        answer = (((i1o[0]*i2o[1]*i3o[2])+(i2o[0]*i3o[1]*i1o[2])+(i1o[1]*i2o[2]*i3o[0]))-((i1o[2]*i2o[1]*i3o[0])+(i1o[0]*i2o[2]*i3o[1])+(i1o[1]*i2o[0]*i3o[2])))

    if space == 3:
        answer4 = ((i4o[3]*(((i1o[0]*i2o[1]*i3o[2])+(i2o[0]*i3o[1]*i1o[2])+(i1o[1]*i2o[2]*i3o[0]))-((i1o[2]*i2o[1]*i3o[0])+(i1o[0]*i2o[2]*i3o[1])+(i1o[1]*i2o[0]*i3o[2])))))
        answer3 = ((i4o[2]*(((i1o[0]*i2o[1]*i3o[3])+(i2o[0]*i3o[1]*i1o[3])+(i1o[1]*i2o[3]*i3o[0]))-((i1o[3]*i2o[1]*i3o[0])+(i1o[1]*i2o[0]*i3o[3])+(i1o[0]*i2o[3]*i3o[1])))))
        answer2 = ((i4o[1]*(((i1o[0]*i2o[2]*i3o[3])+(i2o[0]*i3o[2]*i1o[3])+(i1o[2]*i2o[3]*i3o[0]))-((i1o[3]*i2o[2]*i3o[0])+(i1o[0]*i2o[3]*i3o[2])+(i1o[2]*i2o[0]*i3o[3])))))
        answer1 = ((i4o[0]*(((i1o[1]*i2o[2]*i3o[3])+(i2o[1]*i3o[2]*i1o[3])+(i1o[2]*i2o[3]*i3o[1]))-((i1o[3]*i2o[2]*i3o[1])+(i1o[1]*i2o[3]*i3o[2])+(i1o[2]*i2o[1]*i3o[3])))))
        answer = - answer1 + answer2 - answer3 + answer4
    return(answer)
    #main end
print(matrix())