# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

n = int(input ("Введите количество монет:  "))
a = 0
b = 0

for i in range(n):
    m = int(input("Введите число 1 или 0:  "))
    while m < 0 or m > 1:
        print("Введено неверное число!")
        m = int(input("Введите число 1 или 0:  "))
    if m == 1:
        a += 1
    else: b += 1

if a < b:
    print("Минимальное количество монет, которые нужно перевернуть", a)
else: print("Минимальное количество монет, которые нужно перевернуть", b)