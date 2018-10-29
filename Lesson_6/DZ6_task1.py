
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
        self.player_cards = []
        self.cards_count = cards_count
        for index in range(0, self.cards_count):
            new_card = pack.cards_in_pack.pop()
            self.player_cards.append(new_card)

    def show_cards(self):
        for item in self.player_cards:
            print(item.suit, item.value)

    def add(self, *args):
        self.player_cards.extend(*args)



pack1 = Pack()
pack1.mix()

player1 = Player(4, pack1)
player1.show_cards()



