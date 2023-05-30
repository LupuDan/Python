# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

def count_occurrences(array, x):
    count = 0
    for num in array:
        if num == x:
            count += 1
    return count

N = int(input("Введите количество элементов в массиве: "))

array = []
for i in range(N):
    element = int(input("Введите элемент массива: "))
    array.append(element)

X = int(input("Введите число X: "))

occurrences = count_occurrences(array, X)

print("Число", X, "встречается", occurrences, "раз(а) в массиве.")