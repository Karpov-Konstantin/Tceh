def first_decorator(func):
    def inner(*args):
        print('first_decorator')
        func(*args)
    return inner


def second_decorator(func):
    def inner(*args):
        print('second_decorator')
        func(*args)
    return inner


def third_decorator(func):
    def inner(*args):
        print('third_decorator')
        func(*args)
    return inner


@first_decorator
@second_decorator
@third_decorator
def sum(x, y):
    print(x + y)
    return x + y


sum(1, 2)