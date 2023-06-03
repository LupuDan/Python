# Фибоначчи
# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ...,
# где # a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи

# def sequence(num):
#     if num in [0, 1]:
#         return 1
#     return sequence(num - 1) + sequence(num - 2)

# print(sequence(int(input())))



# Хакер Василий получил доступ к классному
# журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

# 8
# 5 4 2 2 4 2 2 5

# num = int(input())
# grades = list(map(int, input().split()))
# num_max = max(grades)
# num_min = min(grades)

# grades_change = [num_min if j == num_max else j for j in grades]
# print(grades_change)



# Напишите функцию, которая принимает
# одно число и проверяет, является ли оно простым
#
# Напоминание: Простое число - это число,
# которое имеет 2 делителя: 1 и n(само число)

# https://www.delftstack.com/ru/howto/python/python-isprime/

# def prime_num(num):
#     if num == 2 or num == 3: return True
#     if num % 2 == 0 or num < 2: return False
#     for i in range(3, int(num ** 0.5) + 1, 2):
#         if num % i == 0:
#             return False
#     return True


# print(prime_num(int(input())))



# Дано натуральное число N и последовательность
# из N элементов. Требуется вывести эту
# последовательность в обратном порядке.

# Примечание. В программе запрещается
# объявлять массивы и использовать
# циклы (даже для ввода и вывода).


def rev_num(num):
    if num == 0:
        return ""
    nums = input()
    return rev_num(num - 1) + f"{nums} "


print(rev_num(int(input())))