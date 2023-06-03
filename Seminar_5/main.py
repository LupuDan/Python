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

num = int(input())
grades = list(map(int, input().split()))
num_max = max(grades)
num_min = min(grades)

grades_change = [num_min if j == num_max else j for j in grades]
print(grades_change)