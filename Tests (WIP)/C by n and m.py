#!/usr/bin/python3
import sys
import math

try:
    if int(sys.argv[1]) > int(sys.argv[2]):
        exit()
    fact = math.factorial(int(sys.argv[2])) / (math.factorial(int(sys.argv[1])) * math.factorial(int(sys.argv[2]) - int(sys.argv[1])))
except(IndexError):
    m=int(input("Введите m: "))
    n=int(input("Введите n: "))
    if m > n:
        exit()
    fact = math.factorial(n) / (math.factorial(m) * math.factorial(n - m))
print(fact)






