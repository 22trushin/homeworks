def my_function():
    print('I am a function')

print(my_function)
print('Functions are objects', isinstance(my_function, object))


test = my_function
test()


my_list = []
my_list.append(my_function)
print(my_list)
