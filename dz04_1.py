# Написать игру пятнашки.
# Выводится поле размером 4х4. Заполненное случайным образом числами от 1 до 15 в случайном порядке,
# каждое число выводится один раз, одна ячейка остается пустой.

import random


def draw_board(board):
    print('__________')
    print('|' + board[1] + '|' + board[2] + '|' + board[3] + '|' + board[4] + '|')
    print('----------')
    print('|' + board[5] + '|' + board[6] + '|' + board[7] + '|' + board[8] + '|')
    print('----------')
    print('|' + board[9] + '|' + board[10] + '|' + board[11] + '|' + board[12] + '|')
    print('----------')
    print('|' + board[13] + '|' + board[14] + '|' + board[15] + '|' + board[16] + '|')
    print('----------')


def creating_random_list():
    list1 = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','_']
    random.shuffle(list1)
    list1 = ['',] + list1
    return list1


def comanda(key):
    if key == 'up':
        smeshenie = -4
    elif key == 'down':
        smeshenie = 4
    elif key == 'left':
        smeshenie = -1
    elif key == 'right':
        smeshenie = 1
    elif key == 'exit':
        smeshenie = 100
    else:
        print("Вы ввели неправильную команду. Повторите ввод.")
        smeshenie = 0
    return smeshenie

new_list = creating_random_list()
draw_board(new_list)
free_space = new_list.index('_')
print(free_space)
while True:
    if new_list != ['','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','_']:
        key1 = input("Введите команду ('up' or 'down' or 'left' or 'right') \n")
        smeshenie1 = comanda(key1)
        if smeshenie1 == 100:
            break
        vremennaya = new_list[free_space + smeshenie1]
        new_list[free_space + smeshenie1] = '_'
        new_list[free_space] = vremennaya
        print(smeshenie1)
        draw_board(new_list)
        free_space = new_list.index('_')
    else:
        break












