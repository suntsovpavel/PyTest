from user import choose_mode
from work_with_dict import *

def running():
    person, mode, keyword  = choose_mode()
    if mode == 'запись':   # добавление в справочник данных нового лица 
        filling_one_person(person)
        print(f'Данные справочника успешно изменены: {parse_dict()}')
    elif mode == 'поиск':  # поиск человека  по имени либо фамилии и вывод на печать        
        # поиск данных пользователя в справочнике:
        data_user = get_data_from_dict(keyword, parse_dict())
        if not 'name' in data_user:
            print(f'Пользователь с таким именем либо фамилией не найден ({keyword})')
        else:
            print(f'Данные пользователя: {data_user}')             


# по слову поиска (имя или фамилия) ищем из справочника данные человека 
# результат: словарь {'name','second_name','surname','phone'}
def get_data_from_dict(keyword: str, list_dict):
    for one_dict in list_dict:
        if keyword == one_dict['name'] or keyword == one_dict['surname']:
            return one_dict
    return {}   # если ничего не нашли, возвращаем пустой словарь         


