import pygame as pg

from src.config import CARD_WIDTH, CARD_HEIGHT


class SelectImage:

    def __init__(self, type, suit=None, rank=None, color = None):
        self.type = type
        # integer value
        self.color = color

        self.suit = suit
        self.row = self.select_row(suit)

        self.value = rank
        self.col = self.select_col(rank)



    def select_row(self, suit):
        if suit == 'H':
            row = 0
        elif suit == 'D':
            row = 1
        elif suit == 'S':
            row = 2
        elif suit == 'C':
            row = 3
        else:
            row = 4
        return row

    def select_col(self, rank):
        try:
            card = int(rank)
            col = card-1
        except:
            if rank == 'A': col = 0
            elif rank == 'J': col = 10
            elif rank == 'Q': col = 11
            elif rank == 'K': col = 12
            else:
                col = self.color
        return col


    def get_image(self):
        if self.type == "card":
            sprite_sheet = pg.image.load("assets/cards.png").convert_alpha()
            card_rect = pg.Rect(self.col*CARD_WIDTH, self.row*CARD_HEIGHT, CARD_WIDTH, CARD_HEIGHT)
            image = sprite_sheet.subsurface(card_rect).copy()
        elif self.type == "back_card":
            sprite_sheet = pg.image.load("assets/cards.png").convert_alpha()
            card_rect = pg.Rect(self.col*CARD_WIDTH, self.row*CARD_HEIGHT, CARD_WIDTH, CARD_HEIGHT)
            image = sprite_sheet.subsurface(card_rect).copy()

        else:
            sprite_sheet = pg.image.load("assets/cards.png").convert_alpha()
            card_rect = pg.Rect(672, 0, CARD_WIDTH, CARD_HEIGHT)
            image = sprite_sheet.subsurface(card_rect).copy()

        return pg.transform.scale2x(image)


