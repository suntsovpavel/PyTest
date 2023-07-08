# Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

x0 = int(input('Введите первый элемент: '))
delta = int(input('Введите приращение: '))
total = int(input('Введите количество элементов: '))

arr = []
i = 0
while len(arr) < total:
    arr.append(x0 + delta * i)
    i += 1
print(f'Итоговый массив: {arr}')    