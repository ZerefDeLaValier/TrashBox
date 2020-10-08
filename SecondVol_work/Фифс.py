import re
i1 = str(input("Введите 2 числа: "))
i1o = re.split(r' ', i1)
for i in range(len(i1o)):
    i1o[i] = int(i1o[i])
x1 = i1o[0]
x2 = i1o[1]
print("Сумма: ",(x1 + x2))
print("Разность: ",(x1 - x2))
print("Произведение: ",(x1 * x2))
print("Частное: ",(x1 / x2))