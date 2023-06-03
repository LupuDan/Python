# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

# def power(base, exponent):
#     result = 1

#     if exponent < 0:
#         base = 1 / base
#         exponent = -exponent

#     while exponent > 0:
#         result *= base
#         exponent -= 1

#     return result


# A = float(input("Введите число A: "))
# B = int(input("Введите степень B: "))

# result = power(A, B)
# print("Результат возведения", A, "в степень", B, ":", result)


# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.

def sum(a, b):
    if a == 0:
        return b
    if b == 0:
        return a

    if a > 0:
        return sum(a - 1, b + 1)
    else:
        return sum(a + 1, b - 1)


a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

result = sum(a, b)
print("Сумма чисел a и b:", result)