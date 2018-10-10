# Написать “калькулятор”. Пользователь вводит либо числа, либо знаки арифметических действий (+, -, *, /),
# калькулятор выводит промежуточные ответы.
# Первый ввод обязательно число.
# Приоритезации операций нет, скобки не обрабатываются.
# Окончание работы является ввод пустой строки (т.е. просто нажатие Enter)

first_num = ' '
next_input = ' '
next_num = '0'
operator = ''

while True:
    if first_num == ' ':
        while first_num.isdigit() == False:
            first_num = input('Введите число \n')
            if first_num == '':
                next_input = first_num
                break
    if next_input == '':
        break
    next_input = input('Введите число, либо знак арифметических действий (+, -, *, /) \n')
    if next_input.isdigit() == True or next_input == '+' or next_input == '-' or next_input == '*' or next_input == '/':
       if next_input.isdigit() == True:
           next_num = next_input
           if operator != '':
               if operator == '+':
                   first_num = int(first_num) + int(next_input)
                   operator = ''
                   next_num = '0'
               elif operator == '-':
                   first_num = int(first_num) - int(next_input)
                   operator = ''
                   next_num = '0'
               elif operator == '*':
                   first_num = int(first_num) * int(next_input)
                   operator = ''
                   next_num = '0'
               else:
                   if next_input == '0':
                       print('На ноль делить нельзя!')
                       operator = ''
                       next_num = '0'
                   else:
                       first_num = int(first_num) / int(next_input)
                       operator = ''
                       next_num = '0'
               print('Промежуточный итог: ', first_num)
           else:
               print('Действие еще не было введено.')
       else:
           operator = next_input

    elif next_input == '':
        break
    else:
        print('Вы ввели некорректный символ.')


