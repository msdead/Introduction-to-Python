# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[0..N-1]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1

n = int(input ("Введите число (длинна массива):  "))
n = [0] * n
for i in range(len(n)):
    n[i] = int(input("Введите число:  "))
m = int(input ("Введите число которое ищите:  "))
count = 0
for i in range(len(n)):
    if n[i] == m:
        count += 1 
print(count)