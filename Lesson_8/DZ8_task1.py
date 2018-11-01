import random

FIELD = [' ', ' ', ' ', ' ', ' ',   ' ', ' ', ' ', ' ', ' ', \
        ' ', ' ', ' ', ' ', ' ',   ' ', ' ', ' ', ' ', ' ', \
        ' ', ' ', ' ', ' ', ' ',   ' ', ' ', ' ', ' ', ' ', \

        ' ', ' ', ' ', ' ', ' ',   ' ', ' ', ' ', ' ', ' ', \
        ' ', ' ', ' ', ' ', ' ',   ' ', ' ', ' ', ' ', ' ', \

        ' ', ' ', ' ', ' ', ' ',   ' ', ' ', ' ', ' ', ' ', \
        ' ', ' ', ' ', ' ', ' ',   ' ', ' ', ' ', ' ', ' ', \
        ' ', ' ', ' ', ' ', ' ',   ' ', ' ', ' ', ' ', ' ', \

        ' ', ' ', ' ', ' ', ' ',   ' ', ' ', ' ', ' ', ' ', \
        ' ', ' ', ' ', ' ', ' ',   ' ', ' ', ' ', ' ', ' ',  ]

Convvert_input_val = {
'А1':0, 'Б1':1, 'В1':2, 'Г1':3, 'Д1':4, 'Е1':5, 'Ж1':6, 'З1':7, 'И1':8, 'К1':9,\
'А2':10, 'Б2':11, 'В2':12, 'Г2':13, 'Д2':14, 'Е2':15, 'Ж2':16, 'З2':17, 'И2':18, 'К2':19,\
'А3':20, 'Б3':21, 'В3':22, 'Г3':23, 'Д3':24, 'Е3':25, 'Ж3':26, 'З3':27, 'И3':28, 'К3':29,\
'А4':30, 'Б4':31, 'В4':32, 'Г4':33, 'Д4':34, 'Е4':35, 'Ж4':36, 'З4':37, 'И4':38, 'К4':39,\
'А5':40, 'Б5':41, 'В5':42, 'Г5':43, 'Д5':44, 'Е5':45, 'Ж5':46, 'З5':47, 'И5':48, 'К5':49,\
'А6':50, 'Б6':51, 'В6':52, 'Г6':53, 'Д6':54, 'Е6':55, 'Ж6':56, 'З6':57, 'И6':58, 'К6':59,\
'А7':60, 'Б7':61, 'В7':62, 'Г7':63, 'Д7':64, 'Е7':65, 'Ж7':66, 'З7':67, 'И7':68, 'К7':69,\
'А8':70, 'Б8':71, 'В8':72, 'Г8':73, 'Д8':74, 'Е8':75, 'Ж8':76, 'З8':77, 'И8':78, 'К8':79,\
'А9':80, 'Б9':81, 'В9':82, 'Г9':83, 'Д9':84, 'Е9':85, 'Ж9':86, 'З9':87, 'И9':88, 'К9':89,\
'А10':90, 'Б10':91, 'В10':92, 'Г10':93, 'Д10':49, 'Е10':95, 'Ж10':96, 'З10':97, 'И10':98, 'К10':99,\

}


class Player():
    def __init__(self, field, name):
        self.field = list(field)
        self.enemy_field = list(field)
        self.name = name


def print_field (value_field):
    i = 0
    view_str='|'
    index = 1
    print('\n')
    print('  |А|Б|В|Г|Д|Е|Ж|З|И|К|')
    print('-' * 23)

    for item in value_field:
        i += 1
        view_str += str(item) + '|'
        if i == 10:
            if len(str(index)) < 2:
                view_str = ' ' + str(index) + view_str
            else:
                view_str = str(index) + view_str
            index+=1
            print(view_str)
            print ('-'*23)
            view_str = '|'
            i = 0


def put_ships(current_player):
    print('Ходит {}'.format(current_player.name))
    for i in range(0,4):
        try:
            x = input('Введите координаты 4-х палубника: ',)
            convert_x_y = Convvert_input_val[x]
            current_player.field[convert_x_y] = 'U'        # тут корабль
        except Exception as e:
            print('Неправильный ввод, теперь у Вас корабль покороче!')

    current_ships = 0
    while current_ships < 2:
        print('Следующий корабль')
        for i in range(0,3):
            try:
                x = input('Введите координаты 3-х палубника: ', )
                convert_x_y = Convvert_input_val[x]
                current_player.field[convert_x_y] = 'U'
            except Exception as e:
                print('Неправильный ввод, теперь у Вас корабль покороче!')
        current_ships += 1

    current_ships = 0
    while current_ships < 3:
        print('Следующий корабль')
        for i in range(0,2):
            try:
                x = input('Введите координаты 2-х палубника: ', )
                convert_x_y = Convvert_input_val[x]
                current_player.field[convert_x_y] = 'U'
            except Exception as e:
                print('Неправильный ввод, теперь у Вас корабль покороче!')
        current_ships += 1

    current_ships = 0
    while current_ships < 4:
        print('Следующий корабль')
        try:
            x = input('Введите координаты 1-но палубника: ',)
            convert_x_y = Convvert_input_val[x]
            current_player.field[convert_x_y] = 'U'
            current_ships += 1
        except Exception as e:
            print('Неправильный ввод, попробуйте еще раз!')


def attack_enemy_ships(current_player1, current_player2):
    print('Ходит {}'.format(current_player1.name))
    try:
        x = input('Введите координаты вражеского корабля: ', )
        convert_x_y = Convvert_input_val[x]
    except Exception as e:
        print('Неправильный ввод, в следующий раз повезет!')

    if current_player2.field[convert_x_y] == 'U':
        print('Попадание!')
        current_player1.enemy_field[convert_x_y] = 'Y'  # Yes
        current_player2.field[convert_x_y] = 'X'        # Сюда стреляли
        attack_enemy_ships(current_player1, current_player2)
    else:
        print('Промах')
        current_player1.enemy_field[convert_x_y] = 'N'        # No




def main_game (current_player1, current_player2):
    while  True:                                     # проверка на наличие живых кораблей у 1 игрока
        if 'U' not in current_player1.field:
            print('Игрок 2 выиграл')
            return None
            break

        print('Постреляем?')
        attack_enemy_ships(current_player1, current_player2)
        print('Поле соперника')
        print_field(current_player1.enemy_field)

        if 'U' not in current_player2.field:           # проверка на наличие живых кораблей у 1 игрока
            print('Игрок 1 выиграл')
            return None

        print('Постреляем?')
        attack_enemy_ships(current_player2, current_player1)
        print('Поле соперника')
        print_field(current_player2.enemy_field)



player1 = Player(FIELD,'Игрок1')
put_ships(player1)

player2 = Player(FIELD, 'Игрок2')
put_ships(player2)

print_field(player1.field)
print_field(player2.field)


main_game(player1, player2)





