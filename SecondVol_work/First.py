import re
i1 = str(input("Введите длинны двух катетов через пробел: "))
i1o = re.split(r' ', i1)
a = int(i1o[0])
b = int(i1o[1])
outputS = str((a * b)/2)
outputP = str(((a**2 + b**2)**0.5)+a+b)
print("Площадь = "+outputS+" Периметр = "+outputP)
