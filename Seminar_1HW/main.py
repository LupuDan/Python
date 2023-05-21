#Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input("Введите трехзначное число: "))

if number < 100 or number > 999:
    print("Ошибка! Введено неправильное число.")
else:
    digit1 = number // 100  
    digit2 = (number // 10) % 10  
    digit3 = number % 10  

    digit_sum = digit1 + digit2 + digit3

    print("Сумма цифр числа", number, ":", digit_sum)