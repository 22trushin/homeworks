# Задание №2 (посложнее)
# Напишите игру “Поле чудес”
# Пример:
#
# Начинаем играть: _ _ _ _ _ _
# Введите букву: y
# Есть такая буква! : _ y _ _ _ _
# Введите букву: a
# Нет такой буквы!
# Введите букву: y
# Такую букву уже называли!
# Введите букву: p
# Есть такая буква! : p y _ _ _ _
# Введите букву: t
# Есть такая буква! : p y t _ _ _
# Введите букву: h
# Есть такая буква! : p y t h _ _
# Введите букву: o
# Есть такая буква! : p y t h o _
# Введите букву: n
# Поздравляем, вы отгадали слово! : p y t h o n

secret_word = 'python'


def get_guess(already_guessed):
    # Возвращает букву, введенную игроком. Эта функция проверяет, что игрок ввел только одну букву и ничего больше
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in already_guessed:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдеежзийклмнопрстуфхцчшщъыьэюяabcdefghijklmnopqrstuvwxyz':
            print('Пожалуйстаб введите БУКВУ.')
        else:
            return guess


def display_board(missed_letters, correct_letters, secret_word):

    # print('Ошибочные буквы:', end=' ')
    # for letter in missed_letters:
    #    print(letter, end=' ')
    # print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):  # заменяет пропуски отгаданными буквами
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:  # Показывает секретное слово с пробелами между букв
        print(letter, end=' ')
    print()


print('Игра Поле чудес. Попробуйте отгадать слово.')
missed_letters = ''
correct_letters = ''
game_over = False

while True:
    display_board(missed_letters, correct_letters, secret_word)

    # Позволяет игроку ввести букву
    guess = get_guess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters = correct_letters + guess

        # проверяет, выиграл ли игрок
        foundAllLetters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                foundAllLetters = False
                break
        if foundAllLetters:
            print('ДА! Секретное слово - "' + secret_word + '"! Вы угадали!')
            game_over = True
    else:
        missed_letters = missed_letters + guess

    if game_over:
        break
