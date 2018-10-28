def exception_decorator(func):
    def inner(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except ZeroDivisionError as e:
            print('RightError')
        except:
            print('WrongError')
            raise ValueError  # WrongError

    return inner


@exception_decorator
def sum(x, y):
    test_list = [1, ]
    result = x + test_list[1]
    print('Function called, result ', result)
    return result


@exception_decorator
def div(x, y):
    result = x / y
    print('Function called, result ', result)
    return result


div(4, 0)
sum(2, 3)
