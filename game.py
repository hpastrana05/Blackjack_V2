from decks.deck import Deck
from players.player import Player
from players.dealer import Dealer
from states.state_manager import StateManager


class Blackjack:

    def __init__(self, screen):
        self.screen = screen
        self.player = Player("Hugo")
        self.dealer = Dealer()
        self.deck = Deck()
        self.state_manager = StateManager(self.player, self.dealer)


    def draw(self,screen):
        self.player.draw_hand(screen)
        self.dealer.draw_hand(screen)
        self.state_manager.draw(screen)


    def update(self):
        self.state_manager.update()

    def handle_events(self, event):
        self.state_manager.handle_events(event)