# Найдите сумму цифр трехзначного числа.

number = int(input('Введите трехзначное число: '))
if number < 100 or number > 999:
    print(f'Введенное число {number} - не трехзначное')
else:
    sum = number % 10
    while number > 0:
        number = number // 10
        sum += number % 10
    print(f'Сумма цифр равна {sum}')        