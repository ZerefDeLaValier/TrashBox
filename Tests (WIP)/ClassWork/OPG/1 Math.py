a = int(input("A = "))
b = int(input("B = "))
c = int(input("C = "))
try:
    answer = (((((((a+b)**2)/(b**2-c**3))**(1/2)) - ((c**2-c**3+b**a)/((b-c**2+a**b)**(1/2))))/((a**3+b**4-b**a-b**c)**(1/3)))**(a/c))
    #l = ((a+b)**2)/(b**2-c**3)**(1/2)
    #l2 = ((c**2 - c**3 + b**a) / (b-c**2+a**b)) ** (1/2)
    #l3 = ((a**3 + b**4 - b**a - b**c)**(1/3))**(1/3)
except ZeroDivisionError:
    print("Деление на 0")
print(answer)
#print(l2)
#print(l3)