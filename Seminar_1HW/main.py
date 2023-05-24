#Задача 2: Найдите сумму цифр трехзначного числа.

# number = int(input("Введите трехзначное число: "))

# if number < 100 or number > 999:
#     print("Ошибка! Введено неправильное число.")
# else:
#     digit1 = number // 100  
#     digit2 = (number // 10) % 10  
#     digit3 = number % 10  

#     digit_sum = digit1 + digit2 + digit3

#     print("Сумма цифр числа", number, ":", digit_sum)


# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# s = int(input("Введите общее количество журавликов: "))

# x = s // 4

# katya = 2 * (2 * x)

# print("Петя:", x)
# print("Катя:", katya)
# print("Сережа:", x)


# Задача 6: Вы пользуетесь общественным транспортом?
# Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

# ticket_number = input("Введите номер билета (шестизначное число): ")

# if len(ticket_number) != 6:
#     print("Ошибка! Номер билета должен быть шестизначным.")
# else:
#     digits = [int(digit) for digit in ticket_number]

#     sum_first_half = sum(digits[:3])
#     sum_second_half = sum(digits[3:])

#     if sum_first_half == sum_second_half:
#         print("Билет", ticket_number, "является счастливым!")
#     else:
#         print("Билет", ticket_number, "не является счастливым.")



# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

n = int(input("Введите количество долек по горизонтали (n): "))
m = int(input("Введите количество долек по вертикали (m): "))
k = int(input("Введите количество отламываемых долек (k): "))

if k > n * m:
    print("Ошибка! Количество отламываемых долек превышает общее количество долек.")
else:
    if (k % n == 0 and k <= m) or (k % m == 0 and k <= n):
        print("Да, разлом возможен.")
    else:
        print("Нет, разлом невозможен.")