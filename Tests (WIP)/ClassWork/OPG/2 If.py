a = int(input("Введите число: "))
b=0
c = a
if (a > 9) and (a < 100) and (a % 2 == 1):
    print("Число нечетное и двузначное")
else:
    print("Число не соответствует условиям")

if (a >= 0) and (a < 10):
    print(1)
elif (a >= 10) and (a < 100):
    print(2)
elif (a >= 100) and (a < 1000):
    print(3)
elif (a >= 1000) and (a < 10000):
    print(4)
else:
    print("Больше 4 чисел")

while a > 0:
    a = a // 10
    b = b + 1
print(b)

if b == 3:
    First = c // 100
    Second = c // 10
    Second = Second % 10
    Thrid = c % 10
    Final = First+Second+Thrid
    print(Final)