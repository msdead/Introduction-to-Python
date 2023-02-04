# Задача 18: Требуется найти в массиве A[0..N-1] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел A[i]. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6

# -> 5

n = int(input ("Введите число (длинна массива):  "))
n = [0] * n

for i in range(len(n)):
    n[i] = int(input("Введите число:  "))
    
m = int(input ("Введите число которое ищите:  "))
result1 = float('-inf')
result2 = float('inf')

for i in range(len(n)):
    if m == n[i]:
        break    
    if n[i] > m:
        maximum = m - n[i]
        if result1 < maximum:
            result1 = maximum
            answer1 = n[i]
    elif n[i] < m:
        minimum = m - n[i]
        if result2 > minimum:
            result2 = minimum
            answer2 = n[i]
            
if m == n[i]:
    print("Ближайшее число к искомому, указанное число,", m)
elif m - result2 == m + result1:
    print("Ближайшее число к искомому", answer1, 'и', answer2)
elif m - result2 > m + result1:
    print("Ближайшее число к искомому", answer2)
else: print("Ближайшее число к искомому", answer1)