# Написать программу, которая будет задавать пользователю вопросы, и проверять правильность ответов.
# Если пользователь неправильно ответил на вопрос, то выводится сообщение,
# что ответ неверный и вопрос задается повторно.
# Программа должна задавать не менее трех вопросов.
# Вопросы задаются последовательно.
i = 0
a = ''
while a != '1' and i != 3:
    a = input('Сколько астрономических единиц до Солнца от Земли? ')
    i = i + 1
    if a != '1' and i != 3:
        print('Неправильно, попробуйте еще раз.')
    elif a == '1':
        print('Вы дали правильный ответ. Переходим к следующему вопросу.')
    else:
        print('Неправильно, переходим к другому вопросу.')
a = ''
i = 0
while a != 'Бразилиа' and i != 3:
    a = input('Столица Бразилии? ')
    i = i + 1
    if a != 'Бразилиа' and i != 3:
        print('Неправильно, попробуйте еще раз.')
    elif a == 'Бразилиа':
        print('Вы дали правильный ответ. Переходим к следующему вопросу.')
    else:
        print('Неправильно, переходим к другому вопросу.')
a = ''
i = 0
while a != '1024' and i != 3:
    a = input('Сколько байт в килобайте? ')
    i = i + 1
    if a != '1024' and i != 3:
        print('Неправильно, попробуйте еще раз.')
    elif a == '1024':
        print('Вы дали правильный ответ. На этом все, до новых встреч.')
    else:
        print('Неправильно, наберитесь знаний и попробуйте заново. На этом вопросы закончились. До свидания.')