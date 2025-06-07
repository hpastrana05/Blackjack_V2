import pygame as pg
from .player import Player
from config import SCREEN_WIDTH, CARD_WIDTH, CARD_HEIGHT

class Dealer(Player):

        def __init__(self):
            super().__init__("Dealer")
            self.turn = False
            self.draw_time = 0
            self.ended = False

        def should_hit(self):
            return self.hand_value() < 17

        def perform_turn(self):
            now = pg.time.get_ticks()
            self.hand[-1].front_side = True
            if now - self.draw_time >= 500:
                if self.should_hit():
                    self.deal()

                self.ended = not self.should_hit()
                self.draw_time = now



        def draw_hand(self, screen):
            hand_len = len(self.hand)
            half_cards = hand_len / 2
            pos = SCREEN_WIDTH // 2 - half_cards * CARD_WIDTH
            for card in self.hand:
                card.pos = (pos , CARD_HEIGHT)
                card.draw(screen)
                pos += CARD_WIDTH

        def deal_upsidedown(self):
            card = self.deck.deal()
            card.flip_card()
            self.hand.append(card)