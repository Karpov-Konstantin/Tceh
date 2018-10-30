import time


def sum(x, y):
    print('function is called')
    return (x + y)


class Work_Time(object):
    def __init__(self, func,):
        self.func = func

    def __enter__(self, ):
        self.start_time = time.time()
        return self.func

    def __exit__(self, *args):
        self.end_time = time.time()
        print('Work time is ', self.start_time - self.end_time)


with Work_Time(sum) as f:
    f(3, 4)




