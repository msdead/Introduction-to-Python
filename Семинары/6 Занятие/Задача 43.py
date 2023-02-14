# Задача №43.
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.

# Ввод: 
# 1 2 3 2 3 

# Вывод:
# 2

list1 =  list(map(int, input("Введите числа массива через пробел: ").split()))
count = 0

for i in range(len(list1) - 1):
    if list1[i] is None:
        continue
    count_i= 1
    for j in range(i + 1, len(list1)):
        if list1[j] is not None and list1[i] == list1[j]:
            count_i += 1
            list1[j]= None
    count += count_i//2
print(count)

