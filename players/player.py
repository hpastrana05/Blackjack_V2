from config import DEFAULT_CHIPS, SCREEN_WIDTH, SCREEN_HEIGHT, CARD_HEIGHT, CARD_WIDTH
from decks import Deck

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.chips = DEFAULT_CHIPS
        self.deck = Deck()

    def deal(self):
        card = self.deck.deal()
        self.hand.append(card)

    def draw_hand(self, screen):
        hand_len = len(self.hand)
        half_cards = hand_len / 2
        pos = SCREEN_WIDTH // 2 - half_cards*CARD_WIDTH
        for card in self.hand:
            card.pos =(pos, SCREEN_HEIGHT-CARD_HEIGHT*2 - 60)
            card.draw(screen)
            pos += CARD_WIDTH


    def hand_value(self):
        sum = 0
        aces = 0

        for card in self.hand:
            if card.front_side:
                sum += card.value
                if card.rank == 'A':
                    aces += 1

        while sum>21 and aces:
            sum -=10
            aces -= 1

        return sum

    def is_busted(self):
        return self.hand_value() > 21