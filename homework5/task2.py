# 2.Создайте список из случайных чисел. 
# Найдите номер его последнего локального максимума 
# (локальный максимум — это элемент, который больше любого из своих соседей).

def task():
    n = int(input('Введите размер списка: '))
    if n < 2:
        print('Введено число меньше 2')
        return

    # Последовательно добавляем элементы
    print('Введите элементы списка: ')
    arr = []
    for i in range(n):
        arr.append(int(input()))    

    found = False    
    index = n-1     # начинаем с последнего элемента    
    while(index > 0):   # исключаем начальный элемент, у которого только один сосед
        if index == n-1:    # у замыкающего элемента только один сосед слева
            if arr[index] > arr[index-1]: 
                found = True
                break       
        else:            
            if arr[index] > arr[index-1] and arr[index] > arr[index+1]:
                found = True
                break    
        index -= 1
    if not found:
        index = 0     # Единственный оставшийся вариант: начальный элемент                      
    print(f'Последний локальный максимум: {arr[index]}, индекс {index}')

task()






