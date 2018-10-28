class Cached(object):
    cached_dict = {}

    def __init__(self, func):
        self.func = func

    def __call__(self, x, y):
        input_val = str(x)+'+'+str(y)
        if input_val not in Cached.cached_dict:
            Cached.cached_dict[input_val] = self.func(x, y)
            #return self.func(x, y)
        else:
            print('Result is ', Cached.cached_dict[input_val] )


@Cached
def sum(x, y):
    result = x + y
    print('Function called, result ', result)
    return result

sum(2, 3)
sum(4, 5)
sum(2, 3)