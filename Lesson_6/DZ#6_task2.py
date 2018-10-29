
import random


VAL_LIST = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dama', 'Korol', 'Tuz']
SUITE_LIST = [ 'Piki', 'Chervi', 'Kresti', 'Bubi']


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value


class Pack:
    def __init__(self):
        self.cards_in_pack = []
        for suite in SUITE_LIST :
            for val in VAL_LIST:
                new_card = Card(suite, val)
                self.cards_in_pack.append(new_card)

    def mix(self):
        random.shuffle(self.cards_in_pack)



class Player:
    def __init__(self, cards_count, pack):
        self.exist_cards = []
        self.cards_count = cards_count
        for index in range(0, self.cards_count):
            new_card = pack.cards_in_pack.pop()
            self.exist_cards.append(new_card)

    def show_cards(self):
        print('*' * 8)
        # Как вывести имя экземляра класса ? self.__name__ ->  не поддерживается(
        for item in self.exist_cards:
            print(item.suit, item.value)
        print('\n')


    def add(self, pack):
        new_card = pack.cards_in_pack.pop()
        self.exist_cards.append(new_card)

class Table(Player):
    """  Наследуется из Player
    def __init__(self, pack):
        self.exist_cards = []
        for index in range(0, 3):
            new_card = pack.cards_in_pack.pop()
            self.table_cards.append(new_card)

    def show_cards(self):
        for item in self.table_cards:
            print(item.suit, item.value)

    def add(self):
        new_card = pack.cards_in_pack.pop()
        self.table_cards.append(new_card)
    """


pack1 = Pack()
pack1.mix()

player1 = Player(2, pack1)
player1.show_cards()

player2 = Player(2, pack1)
player2.show_cards()

table1 = Table(3, pack1)
table1.show_cards()

player1.add(pack1)
player2.add(pack1)
player1.show_cards()
player2.show_cards()

table1.add(pack1)
table1.show_cards()



