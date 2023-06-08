# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a1 = int(input("Введите первый элемент прогрессии: "))
# d = int(input("Введите разность прогрессии: "))
# n = int(input("Введите количество элементов: "))

# progression = []

# for i in range(n):
#     element = a1 + (i * d)
#     progression.append(element)

# print("Арифметическая прогрессия:")
# for element in progression:
#     print(element)



# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def find_indices(arr, minimum, maximum):
    indices = []
    for i in range(len(arr)):
        if minimum <= arr[i] <= maximum:
            indices.append(i)
    return indices

my_list = [1, 5, 3, 8, 6, 2, 7, 9, 4]
min_value = 3
max_value = 7

result = find_indices(my_list, min_value, max_value)
print("Индексы элементов, принадлежащих диапазону [{}, {}]:".format(min_value, max_value))
print(result)