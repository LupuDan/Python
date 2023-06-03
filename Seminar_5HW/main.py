# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

def power(base, exponent):
    result = 1

    if exponent < 0:
        base = 1 / base
        exponent = -exponent

    while exponent > 0:
        result *= base
        exponent -= 1

    return result


A = float(input("Введите число A: "))
B = int(input("Введите степень B: "))

result = power(A, B)
print("Результат возведения", A, "в степень", B, ":", result)