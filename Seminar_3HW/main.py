# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# def count_occurrences(array, x):
#     count = 0
#     for num in array:
#         if num == x:
#             count += 1
#     return count

# N = int(input("Введите количество элементов в массиве: "))

# array = []
# for i in range(N):
#     element = int(input("Введите элемент массива: "))
#     array.append(element)

# X = int(input("Введите число X: "))

# occurrences = count_occurrences(array, X)

# print("Число", X, "встречается", occurrences, "раз(а) в массиве.")


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai.
# Последняя строка содержит число X

def find_closest_element(array, x):
    closest_element = array[0]
    min_difference = abs(x - array[0])
    
    for num in array:
        difference = abs(x - num)
        if difference < min_difference:
            min_difference = difference
            closest_element = num
    
    return closest_element

N = int(input("Введите количество элементов в массиве: "))

array = []
for i in range(N):
    element = int(input("Введите элемент массива: "))
    array.append(element)

X = int(input("Введите число X: "))

closest_element = find_closest_element(array, X)

print("Самый близкий элемент к числу", X, "в массиве:", closest_element)