import random

from DZ4_task1_ver2 import WINNER_FIELD, field, print_field,  start_the_game


def check_solution(field):
    chaos_count = 0
    for index, item in enumerate(field):
        if item == ' ':
            if index in (0,4):    # пустая клетка в 1 ряду
                chaos_count += 1
            elif index in (4,8):  # пустая клетка во 2 ряду
                chaos_count += 2
            elif index in (8,12): # пустая клетка в 3 ряду
                chaos_count += 3
            else:                 # пустая клетка в 4 ряду
                chaos_count += 4

        else:
            for index_inner in range(index+1, 16): # идем по элементам, расположенным за эл-том field[index]
                if field[index_inner] == ' ':
                    pass
                elif field[index_inner] < item:
                    chaos_count += 1


    if (chaos_count % 2 == 0):
        print('Пятнашки соберутся')
    else:
        print('Пятнашка не соберутся :C ')








if __name__ == '__main__' :
    random.shuffle(field)
    check_solution(field)
    start_the_game()
