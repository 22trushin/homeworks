import re


def way_better(filename):  # Функция читающая файл
    print('reading file with way_better()')
    try:
        with open(filename) as f:
            return f.read()
    except FileNotFoundError:
        print('File not found')


def count_entry(list1):  # Функция подсчитывающая количество вхождений одинаковых записей в список
    count_dict = {}
    count = 0
    value = 0

    while count < len(list1):
        if list1[count] not in count_dict.keys():
            for item in list1:
                if item == list1[count]:
                    value += 1
            count_dict.update({list1[count]: value})
        count += 1
        value = 0
    return count_dict


def results(dict1):  # Функция ввыводящая результат в консоль в виде таблицы
    for k, v in dict1.items():
        print('| ', k, ' | ', v, ' |')
    print()


raw_text = way_better('nasa_19950801.tsv')  # Читаем нужный файл

name_pattern_group = r'.*\s(\d*)\tGET\t(.*)\s(\d\d\d)\s\d.*'  # Шаблон регулярного выражения
ready_text = re.findall(name_pattern_group, raw_text)  # Ищем по шаблону текст

# f = open('nasa_ready_text.txt', 'w')
# f.write(str(ready_text))
# f.close()

print('Number of rows: ', len(ready_text))

# Формируем отдельные списки из полученого
x = 0
url_list = []
time_list = []
code_list = []
while x < len(ready_text):
    time_list.append(ready_text[x][0])
    url_list.append(ready_text[x][1])
    code_list.append(ready_text[x][2])
    x += 1
# print(time_list)
# print(time_list, '\n', url_list, '\n', code_list)

# Считаем вхождения и выводим в консоль
count_dict_code = count_entry(code_list)
print('| Код ошибки | Количество ошибок |')
results(count_dict_code)
count_dict_time = count_entry(time_list)
print('| Timestamp | Количество записей |')
results(count_dict_time)
count_dict_url = count_entry(url_list)
print('| URL | Количество записей |')
results(count_dict_url)

