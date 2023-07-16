name_dict = 'homework8/dict.txt'

# добавление данных нового лица
def filling_one_person(person):
    with open(name_dict, 'a', encoding='utf-8')  as f:
        f.write(person['surname'] + '\n')
        f.write(person['name'] + '\n')
        f.write(person['second_name'] + '\n')
        f.write(person['phone']  + '\n')
        f.write('\n')    

# полностью перезаписывам файл из списка словарей {'name','second_name','surname','phone'}
def filling_all(list_dict):    
    with open(name_dict, 'w', encoding='utf-8')  as f:
        for one_dict in list_dict:
            f.write(one_dict['surname'] + '\n')
            f.write(one_dict['name'] + '\n')
            f.write(one_dict['second_name'] + '\n')
            f.write(one_dict['phone']  + '\n')
            f.write('\n')    

# Считываем содержимое справочника в список словарей {'name','second_name','surname','phone'} и возвращаем его
def parse_dict():
    with open(name_dict, 'r', encoding='utf-8') as f:
        list_dict = []
        count = 0
        name: str; surname: str; second_name: str; phone: str;
        for line in f.read().splitlines():
            # Пропускаем строки-переносы:
            if len(line) == 0:
                continue
            if count == 0:
                surname = line
            elif count == 1:
                name = line
            elif count == 2:
                second_name = line
            else:
                phone = line    
                list_dict.append({'name':name,
                               'second_name':second_name,
                               'surname':surname,
                               'phone':phone})
                count = 0
                continue
            count += 1  
    return list_dict          