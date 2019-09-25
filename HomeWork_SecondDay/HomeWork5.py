#!/usr/bin/python3
obj = [0,0,""]
obj[1] = int(input("Write a First number: "))
obj[2] = int(input("Write a Second number: "))
obj[0] = str(input("Write a math operator (*,/,+,-): "))
try:
    if obj[0] == "/":
        out = obj[1] / obj[2]
    elif obj[0] == "*":
        out = obj[1] * obj[2]
    elif obj[0] == "+":
        out = obj[1] + obj[2]
    elif obj[0] == "-":
        out = obj[1] * obj[2]
    else:
        print("Undefined operator")
        exit()
    print(out)
except ZeroDivisionError:
	print("The Offspring - Dividing By Zero")