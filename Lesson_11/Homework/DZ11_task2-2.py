
def sum(x, y):
    print('function is called')
    return (x + y)


class Work_Time(object):
    def __init__(self, func, x, y):
        self.func = func
        self.x = x
        self.y = y

    def __enter__(self, ):
        self.start_time = time.time()
        try:
            return self.func(self.x, self.y)
        except Exception as e:
            print('Error here')
            return None

    def __exit__(self, *args):
        pass


with Work_Time(sum, 3, None) as f:
    pass


