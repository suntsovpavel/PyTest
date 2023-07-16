from user import choose_mode, fill_person
from model_dict import *

def running():
    person, mode, keyword  = choose_mode()
    if mode == 'запись':   # добавление в справочник данных нового лица 
        filling_one_person(person)
        print(f'Данные справочника успешно изменены: {parse_dict()}')
    elif mode == 'поиск':  # поиск человека  по имени либо фамилии и вывод на печать        
        # поиск данных пользователя в справочнике:
        data_user, index = get_data_from_dict(keyword, parse_dict())
        if index == -1:
            print(f'Пользователь с таким именем либо фамилией не найден ({keyword})')
        else:
            print(f'Данные пользователя: {data_user}')             
    elif mode == 'изменение': 
         # поиск данных пользователя в справочнике:
        dict_content = parse_dict()
        data_user, index = get_data_from_dict(keyword, dict_content)
        if index == -1:
            print(f'Пользователь с таким именем либо фамилией не найден ({keyword})')
        else:
            print(f'Пользователь найден. Введите новые данные:')          
            person = fill_person()
            # Заменяем данные:            
            dict_content[index] = person
            # Перезаписываем справочник:
            filling_all(dict_content)
            print(f'Данные справочника успешно изменены: {parse_dict()}')
    else:  # оставшийся вариант: удаление
         # поиск данных пользователя в справочнике:
        dict_content = parse_dict()
        data_user, index = get_data_from_dict(keyword, dict_content)
        if index == -1:
            print(f'Пользователь с таким именем либо фамилией не найден ({keyword})')
        else:
            print(f'Пользователь найден. Эти данные будут удалены: {data_user}')          
            # Удаляем элемент по индексу
            del  dict_content[index]                   
            # Перезаписываем справочник:
            filling_all(dict_content)
            print(f'Данные справочника успешно изменены: {parse_dict()}')            


# по слову поиска (имя или фамилия) ищем данные человека в справочника 
# результат: словарь {'name','second_name','surname','phone'} и индекс в списке
def get_data_from_dict(keyword: str, list_dict):
    for index,el in enumerate(list_dict):
        # !!! Не проверяем, имеется ли несколько лиц, подходящих под слово поиска. Возвращаем первого встречного
        if keyword == el['name'] or keyword == el['surname']:
            return el, index    
    return {}, -1       # если ничего не нашли, возвращаем пустой словарь и условный индекс -1        


