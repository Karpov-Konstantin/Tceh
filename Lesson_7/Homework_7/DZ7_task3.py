def check(func):
    def inner(*args, **kwargs):
        for val in args:
            print('Input type is ', type(val))

        for val in kwargs:
            print('Input type is ', type(val))

        result = func(*args, **kwargs)
        print('Reuslt type is ', type(result))
        return result

    return inner


@check
def sum(x, y):
    result = x + y
    print('Function called, result ', result)
    return result


sum(2, 3)
sum(4, 5)
sum(2, 3)