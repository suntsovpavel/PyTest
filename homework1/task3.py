# Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, 
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no

number = int(input('Введите шестизначное число: '))
if number < 100000 or number > 999999:
    print(f'Введенное число {number} - не шестизначное')
else:
    count = 0
    sum = number % 10
    sum2 = 0
    while number > 0:
        number = number // 10
        if count < 2:    # первые 2 прохода цикла: суммируем вторую и третью цифры числа справа
            sum += number % 10    
        else:
            sum2 += number % 10               
        count += 1

    answer = 'yes' if (sum == sum2) else 'no'
    print(answer)
