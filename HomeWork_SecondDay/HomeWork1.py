#/usr/bin/python3
a = int(input("Write a number \n"))
if (a > 0) and (a % 2 != 0):
    print("This number is positive and odd")
elif (a > 0) and (a % 2 == 0):
    print("This number is positive and even")
elif (a < 0) and (a % 2 != 0):
    print("This number is negative and odd")
else:
    print("This number is negative and even")