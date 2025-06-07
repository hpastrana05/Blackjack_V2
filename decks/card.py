
from assets.select_image import SelectImage

class Card:

    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value
        self.front_side = True
        self.image = self.load_image()
        self.back_image = self.load_back_image()
        self.pos = (0,0)

    def load_image(self):
        select_image = SelectImage('card', self.suit, self.rank)
        return select_image.get_image()

    def load_back_image(self):
        back_image = SelectImage('back_card', color=0)
        return back_image.get_image()

    def draw(self, screen):
        if self.front_side:
            screen.blit(self.image, self.pos)
        else:
            screen.blit(self.back_image, self.pos)

    def flip_card(self):
        self.front_side = not self.front_side