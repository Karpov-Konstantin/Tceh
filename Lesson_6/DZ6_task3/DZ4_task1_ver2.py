import random

WINNER_FIELD = [1, 2, 3, 4, \
                5, 6, 7, 8, \
                9, 10, 11, 12, \
                13, 14, 15, ' ']

field = [1, 2, 3, 4, \
         5, 6, 7, 8, \
         9, 10, 11, 12, \
         13, 14, 15, ' ']


def print_field(value_field):
    i = 0
    view_str = '|'
    for item in value_field:
        i += 1
        if len(str(item)) > 1:
            view_str += str(item) + '|'
        else:
            view_str += ' ' + str(item) + '|'

        if i == 4:
            print(view_str)
            print('-' * 13)
            view_str = '|'
            i = 0


def start_the_game():
    print_field(field)  # Вывод поля

    while True:
        empty_box_index = field.index(' ')
        action = input('Введите направление смещения ячейки ')
        if action == 'left':
            if (empty_box_index not in (0, 4, 8, 12)):
                field[empty_box_index] = field[empty_box_index - 1]
                field[empty_box_index - 1] = ' '
                print_field(field)
            else:
                print('Ячейку сдвинуть влево нельзя!')


        elif action == 'right':
            if (empty_box_index not in (3, 7, 11, 15)):
                field[empty_box_index] = field[empty_box_index + 1]
                field[empty_box_index + 1] = ' '
                print_field(field)
            else:
                print('Ячейку сдвинуть вправо нельзя!')


        elif action == 'up':
            if (empty_box_index not in (range(4))):
                field[empty_box_index] = field[empty_box_index - 4]
                field[empty_box_index - 4] = ' '
                print_field(field)
            else:
                print('Ячейку сдвинуть вверх нельзя!')


        elif action == 'down':
            if (empty_box_index not in (range(12, 16))):
                field[empty_box_index] = field[empty_box_index + 4]
                field[empty_box_index + 4] = ' '
                print_field(field)
            else:
                print('Ячейку сдвинуть вниз нельзя!')
        else:
            print('Нет такой команды!')

        if field == WINNER_FIELD:
            return ('Ура, победа!')


if __name__ == '__main__':
    random.shuffle(field)
    start_the_game()
