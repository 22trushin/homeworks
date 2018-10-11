# Задание №1 (простое)
# Напишите программу, которая проверяет, является ли введенная строка панграммой
# (т.е. содержит все буквы либо русского, либо английской алфавита)
# Пример русской панграммы - Широкая электрификация южных губерний даст мощный толчок подъёму сельского хозяйства.
# Пример английской - The quick brown fox jumps over the lazy dog
# Расширенный вариант - выводится, каких букв алфавита не хватает во фразе

text = input('Введите панграмму для проверки: \n')
rus_alphabet = ('а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т',
                'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ъ', 'ь', 'э', 'ю', 'я')
eng_alphabet = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')

text = text.lower()
no_symbols = list()
rus_alphabet_list = list()
for item in rus_alphabet:
    if text.find(item) < 0:
        no_symbols += item
for item2 in rus_alphabet:
    rus_alphabet_list += item2
if no_symbols == rus_alphabet_list:
    no_symbols = list()
    for item3 in eng_alphabet:
        if text.find(item3) < 0:
            no_symbols += item3
if no_symbols == list():
    print('Поздравляем у вас панграмма! ')
else:
    print('Увы, вам не хватает таких букв для панграммы: ', no_symbols)
