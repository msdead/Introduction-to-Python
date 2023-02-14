# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым

# Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число)

def is_simple_number(n):
    n = abs(n)
    if n < 2: 
        return "NO"
    for i in range(2, n):
        if n % i == 0:
            return "NO"
    return "YES"

n = int(input("Enter number: "))
print(is_simple_number(n))