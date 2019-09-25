#/usr/bin/python3
a = int(input("Write a number \n"))
if (a % 3 == 0):
    print("The number is a multiple of three")
else:
    print("The number isn't a multiple of three\n", "Remainder of the division:", a % 3)
