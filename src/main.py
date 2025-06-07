import pygame as pg
from game import Blackjack
from config import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR


def main():
    pg.init()
    screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Blackjack")
    clock = pg.time.Clock()
    game = Blackjack(screen)

    run = True
    while run:
        """Game loop:
        draw all elements
        update everything"""

        #Screen Refresh color
        screen.fill(BACKGROUND_COLOR)

        # Handle events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
            else:
                game.handle_events(event)

        game.update()
        game.draw(screen)

        #updates screen
        pg.display.update()
        clock.tick(60)

    pg.quit()

if __name__ == "__main__":
    main()