# Написать “калькулятор”. Пользователь вводит либо числа, либо знаки арифметических действий (+, -, *, /),
# калькулятор выводит промежуточные ответы.
# Первый ввод обязательно число.
# Приоритезации операций нет, скобки не обрабатываются.
# Окончание работы является ввод пустой строки (т.е. просто нажатие Enter)

a = None
b = None
operator = None
i = 0

while a == None:
    a = input('Введите первое число: ')
    if a == '':
        exit()

    a = int(a)

while a != '' and b != '' and operator != '':

    while operator == None:
        operator = input('Введите знак арифмитического действия (+, -, *, /) ')
        if operator == '':
            exit()

    while b == None:
        b = input('Введите следующее число: ')
        if b == '':
            exit()
        b = int(b)
        if operator == '+':
            a = a + b
        elif operator == '-':
            a = a - b
        elif operator == '*':
            a = a * b
        elif operator == '/':
            a = a / b
        else:
            print('Введеный вами знак арифмитического действия не распознан')
        print('Предварительный результат:', a)
        operator = None
    b = None


