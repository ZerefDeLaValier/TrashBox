#/usr/bin/python3
# Технически это код для работает для любого n-значного числа.
# Просто мне лень писать код именно под 4-х значное число, ибо придется писать больше формул.
# Импровизируй, адаптируйся, выживай.
a = int(input("Write a 4-digit number: \n"))
c = 0
while (a > 0):
    c += a % 10
    a = a // 10
print("Sum is:", c)