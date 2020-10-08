import re
i1 = str(input("Введите 4 координаты точек: "))
i1o = re.split(r' ', i1)

for i in range(len(i1o)):
    i1o[i] = int(i1o[i])
x1 = i1o[0]
y1 = i1o[1]
x2 = i1o[2]
y2 = i1o[3]

print(((x2-x1)**2+(y2-y1)**2)**0.5)

