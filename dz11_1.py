import random
import os
from flask import Flask
app = Flask(__name__)

random.seed(os.environ['FLASK_RANDOM_SEED'])
# SECRET_NUMBER = random.randint(1, 100)

# app.config['SECRET_NUMBER'] = random.randint(1, 100)
app.config['GOOD_RESULT_COUNT'] = 0


@app.route('/', methods=['GET', ])
def home_get():
    app.config['SECRET_NUMBER'] = random.randint(1, 100)
    app.config['REQUEST_COUNT'] = 0
    return 'Число загадано!', 200


@app.route('/guess/<int:number>', methods=['POST'])
def home_post(number):
    result_of_check = check(app.config['SECRET_NUMBER'], number)
    ls = [result_of_check, number, app.config['SECRET_NUMBER']]
    app.config['REQUEST_COUNT'] += 1
    if result_of_check == '=':
        app.config['GOOD_RESULT_COUNT'] += 1
    print('Число попыток: ', app.config['REQUEST_COUNT'],
          'Число правильных ответов: ', app.config['GOOD_RESULT_COUNT'])
    return '{}'.format(ls)


def check(secret_number1, user_num):
    if user_num < secret_number1:
        answer = '<'
    elif user_num > secret_number1:
        answer = '>'
    else:
        answer = '='
    return answer


if __name__ == '__main__':

    app.run()