# Вывод n-ного числа Фибоначчи через рекурсию

def f(N):
    if N <= 1:
        return N
    else:
        return f(N - 1) + f(N - 2)

N = int(input("Enter N: "))
print (f"f({N}) = {f(N)}")