# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

n = int(input("Введите количество оценок: "))

grades = [0] * n

for i in range(n):
    grades[i] = int(input("Введите оценку: "))
max_num = max(grades)
min_num = min(grades)

for i in range(n):
    if grades[i] == max_num:
        grades[i] = min_num
print(grades)