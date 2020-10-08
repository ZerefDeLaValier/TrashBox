import re
i1 = str(input("Введите через пробел x1, y1, x2, y2, x3, y3: "))
i1o = re.split(r' ', i1)
for i in range(len(i1o)):
    i1o[i] = int(i1o[i])
x1 = i1o[0]
y1 = i1o[1]
x2 = i1o[2]
y2 = i1o[3]
x3 = i1o[4]
y3 = i1o[5]

a = ((x2-x1)**2 + (y2-y1)**2)**0.5
b = ((x3-x2)**2 + (y3-y2)**2)**0.5
c = ((x3-x1)**2 + (y3-y1)**2)**0.5

P = a+b+c
p2 = P/2
S = (p2*(p2-a)*(p2-b)*(p2-c))**0.5

print("Периметр: ", P)
print("Площадь: ", S)