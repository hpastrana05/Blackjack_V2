import pygame as pg

class State:

    def __init__(self, name):
        self.state_name = name
        self.buttons = self.load_buttons()
        self.text = self.load_text()

    def load_buttons(self)-> dict[str, tuple[pg.Rect, pg.Color]]:
        buttons = {}
        return buttons

    def load_text(self) -> list[tuple[pg.Surface, pg.Rect]]:
        text = []
        return text

    def draw(self, screen):
        for button in self.buttons.values():
            pg.draw.rect(screen, button[1], button[0])

        for text, text_rect in self.text:
            screen.blit(text, text_rect)

    def handle_events(self,event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                for key, rect in self.buttons.items():
                    if rect[0].collidepoint(event.pos):
                        print(f"Cliked button {key}")