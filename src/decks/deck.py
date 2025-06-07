import random
from .card import Card


class Deck:
    class _Deck:
        def __init__(self):
            self.cards = self.create_deck()
            self.all_cards = self.create_deck()


        def restart_deck(self):
            self.cards = []
            for card in self.all_cards:
                card.front_side = True
                self.cards.append(card)

        def create_deck(self):
            suits =['S', 'D', 'C', 'H']
            values = {'A': 11, '2': 2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
            ranks = values.keys()

            cards = []
            for suit in suits:
                for rank in ranks:
                    cards.append(Card(suit, rank, values[rank]))

            return cards

        def shuffle(self):
            random.shuffle(self.cards)

        def deal(self):
            return self.cards.pop()

    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance  = cls._Deck()
        return cls.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)

    def __setattr__(self, key, value):
        return setattr(self.instance, key, value)