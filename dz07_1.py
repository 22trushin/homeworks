# ДЗ 07 задание 1


palindromos = 'saippuakauppias'

list_of_palindromos = [i for i in palindromos]
reverse_list = list_of_palindromos[::-1]
###################### variant 1 ###############

def bar(s):
    st = []
    for i in s:
        st.append(i)
    return st


def compare(x):
    return x[0] == x[1]


f = list(filter(compare, map(bar, [list_of_palindromos[i] + reverse_list[i] for i in range(len(list_of_palindromos))])))
print(f)

###################### variant 2 ###############

many_palindromos_list = ['geeks', 'geeg', 'keek', 'practice', 'aa', 'saippuakauppias', ]

result = list(filter(lambda x: (x == "".join(reversed(x))), many_palindromos_list))

print(result)

# print(reduce(lambda x, y: x + y, list_of_palindromos))
# print(list(filter(lambda x: x <= (len(list_of_palindromos) // 2), range(0, len(list_of_palindromos)))))
# print(list(map(lambda i: x.append(list_of_palindromos[i]), list(filter(lambda x: x <=
# (len(list_of_palindromos) // 2), range(0, len(list_of_palindromos)))))))

# так и не понял как простое выражение ниже можно представить через map + filter + reduce (((


def foo2(lop):
    pol = lop[::-1]
    if pol == lop:
        result1 = True
    else:
        result1 = False
    return 'Перед вами палином: ' + str(result1)


print(foo2(list_of_palindromos))
print()
print()

###################### decorators ###############


def first_decorator(func):
    print('first_decorator writes: ', first_decorator.__name__)

    def wrapped_upper_decorator(internal_decor, internal_func, *args, **kwargs):
        return func(internal_decor, internal_func, *args, **kwargs)
    return wrapped_upper_decorator


def second_decorator(func):
    print('second_decorator writes: ', second_decorator.__name__)

    def wrapped_decorator(internal_func, *args, **kwargs):
        return func(internal_func, *args, **kwargs)
    return wrapped_decorator


def third_decorator(func):
    print('third_decorator writes: ', third_decorator.__name__)

    def wrapped(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapped


@first_decorator
@second_decorator
@third_decorator
def foo(*args, **kwargs):
    print(args, kwargs)


foo(4, 5, 6)
