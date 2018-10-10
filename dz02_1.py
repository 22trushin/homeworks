# Написать программу, которая будет задавать пользователю вопросы, и проверять правильность ответов.
# Если пользователь неправильно ответил на вопрос, то выводится сообщение,
# что ответ неверный и вопрос задается повторно.
# Программа должна задавать не менее трех вопросов.
# Вопросы задаются последовательно.

# dz2 Модифицировать программу из домашнего задания №1 так, чтобы:
# поддерживалось несколько вариантов верных ответов,
# вопросы и ответы лежали в словаре

general_dict = {'question1': 'Сколько астрономических единиц до Солнца от Земли?', 'question2': 'Столица Бразилии?',
                'question3': 'Сколько байт в килобайте?',
                'answer_q1_1': '1', 'answer_q1_2': 'One', 'answer_q1_3': 'одна', 'answer_q2_1': 'Бразилиа',
                'answer_q2_2': 'бразилиа', 'answer_q2_3': 'Brazilia',
                'answer_q3_1': '1024', 'answer_q3_2': '1000+24', 'answer_q3_3': '2^10'
                }


i = 0
a = ''
while a != general_dict['answer_q1_1'] and a != general_dict['answer_q1_2'] and a != general_dict['answer_q1_3'] and i != 3:
    a = input(general_dict['question1'] + ' \n')
    i = i + 1
    if a not in general_dict.values() and i != 3:
        print('Неправильно, попробуйте еще раз.')
    elif a == general_dict['answer_q1_1'] or a == general_dict['answer_q1_2'] or a == general_dict['answer_q1_3']:
        print('Вы дали правильный ответ. Переходим к следующему вопросу.')
    else:
        print('Неправильно, переходим к другому вопросу.')
a = ''
i = 0
while a != general_dict['answer_q2_1'] and a != general_dict['answer_q2_2'] and a != general_dict['answer_q2_3'] and i != 3:
    a = input(general_dict['question2'] + ' \n')
    i = i + 1
    if a not in general_dict.values() and i != 3:
        print('Неправильно, попробуйте еще раз.')
    elif a == general_dict['answer_q2_1'] or a == general_dict['answer_q2_2'] or a == general_dict['answer_q2_3']:
        print('Вы дали правильный ответ. Переходим к следующему вопросу.')
    else:
        print('Неправильно, переходим к другому вопросу.')
a = ''
i = 0
while a != general_dict['answer_q3_1'] and a != general_dict['answer_q3_2'] and a != general_dict['answer_q3_3'] and i != 3:
    a = input(general_dict['question3'] + ' \n')
    i = i + 1
    if a not in general_dict.values() and i != 3:
        print('Неправильно, попробуйте еще раз.')
    elif a == general_dict['answer_q3_1'] or a == general_dict['answer_q3_2'] or a == general_dict['answer_q3_3']:
        print('Вы дали правильный ответ. На этом все, до новых встреч.')
    else:
        print('Неправильно, наберитесь знаний и попробуйте заново. На этом вопросы закончились. До свидания.')
