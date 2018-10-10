# Есть текст, который лежит в string.
# Надо убрать из него все знаки препинания, и найти сколько раз встречается каждое слово.
# Вывести TOP-10 самых встречающихся слов, с указанием, какое это слово и сколько раз оно встретилось.

text_str = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam " \
           "rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt " \
           "explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia " \
           "consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui " \
           "dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora " \
           "incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum " \
           "exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem " \
           "vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel " \
           "illum qui dolorem eum fugiat quo voluptas nulla pariatur?"

str_without_punct = ''
punctuation = ('!', '.', ',', '?', ';', ':', '(', ')', '-')
count = 0
# удаляем все знаки препинания из строки и создаем новую строку
while count < len(text_str):
    if text_str[count] not in punctuation:
        str_without_punct += text_str[count]
    count += 1
print(str_without_punct)

# создаем из строки список слов по разделителю "пробел"
probel = ' '
temp_word = ''
list_of_words = list()
count = 0

while count < len(str_without_punct):
    if str_without_punct[count] != probel:
        temp_word += str_without_punct[count]
    else:
        list_of_words.append(temp_word)
        temp_word = ''
    count += 1

list_of_words.append(temp_word)
print(list_of_words)

# подсчитываем сколько раз слово встречается в списке и формируем словарь на основе этого действа
count_dict = {}
count = 0
value = 0

while count < len(list_of_words):
    if list_of_words[count] not in count_dict.keys():
        for item in list_of_words:
            if item == list_of_words[count]:
                value += 1
        count_dict.update({list_of_words[count]: value})
    count += 1
    value = 0
print(count_dict)

# преобразуем словарь в список кортежей отсортированных по значению
sorted_by_value = sorted(count_dict.items(), key=lambda kv: kv[1])
print(sorted_by_value)

# выводим топ 10 встречаемых слов
x = 0
while x < 10:
    k, v = sorted_by_value.pop()
    print(k, v)
    x += 1

