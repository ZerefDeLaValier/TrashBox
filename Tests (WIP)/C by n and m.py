import sys
import math
try:
    fact = math.factorial(int(sys.argv[2])) / (math.factorial(int(sys.argv[1])) * math.factorial(int(sys.argv[2]) - int(sys.argv[1])))
except(IndexError):
    m=int(input("Введите m: "))
    n=int(input("Введите n: "))
    fact = math.factorial(n) / (math.factorial(m) * math.factorial(n - m))
print(fact)






