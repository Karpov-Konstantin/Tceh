import time

str1 = 'topotsk'
str2 = 'topot'



def work_time (enabled = True):
    def work_time_inner(func):
        def inner(*args):  # кол-во переменных во внутр функции
            if enabled is True:
                start_time = time.time()
                func(*args)
                end_time = time.time()
                print('Work time is ', start_time - end_time)
            else:
                func(*args)
        return inner
    return work_time_inner

@work_time (enabled = True)
def check_str(val_str):
    half_str = int(len(val_str) / 2)
    str1 = val_str[0: half_str]
    str2 = (val_str[-1: half_str - 1: -1])

    flag = 1
    for index in range(half_str):
        if (str1[index] != str2[index]):
            print('Ne polyndrom')
            return False

    print('Polyndrom')
    return True


check_str(str1)
check_str(str2)