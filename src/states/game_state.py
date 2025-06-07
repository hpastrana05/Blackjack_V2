import pygame as pg
from src.config import (NEXT_COLOR, STAND_COLOR, HIT_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT,
                        BUTTON_WIDTH, BUTTON_HEIGHT, SCREEN_CENTER, TEXT_PLAYER_POINTS_POS, TEXT_DEALER_POINTS_POS)
from src.decks.deck import Deck
from src.states.state import State


class GameState(State):
    def __init__(self, player, dealer):
        self.new_game = True
        self.ended = False
        self.deck = Deck()
        self.player = player
        self.dealer = dealer
        super().__init__("game_state")



    def load_buttons(self):
        #Creates the buttons for game screen
        hit_button = pg.Rect(0, 0, BUTTON_WIDTH, BUTTON_HEIGHT)
        stand_button = pg.Rect(0, 0, BUTTON_WIDTH, BUTTON_HEIGHT)
        next_button = pg.Rect(0, 0, BUTTON_WIDTH, BUTTON_HEIGHT)

        # Center the buttons positions
        list_buttons = [ hit_button, stand_button, next_button]
        self.center_buttons(list_buttons)

        buttons = {
            "hit_button": (hit_button, HIT_COLOR),
            "stand_button": (stand_button, STAND_COLOR),
            "next_button": (next_button, NEXT_COLOR),
        }

        return buttons

    def center_buttons(self, buttons):
        # center the buttons on screen
        n_buttons = len(buttons) + len(buttons)//2
        half_buttons = n_buttons // 2
        pos = SCREEN_WIDTH // 2 - half_buttons*BUTTON_WIDTH
        for button in buttons:
            button.center = (pos, SCREEN_HEIGHT // 2)
            pos += BUTTON_WIDTH*2

    def load_text(self):
        #Creates the texts for game screen
        font = pg.font.SysFont(None, 25)

        hit_rect = self.buttons["hit_button"][0]
        stand_rect = self.buttons["stand_button"][0]
        next_rect = self.buttons["next_button"][0]

        # Creates the text
        text_hit = font.render("HIT", True, "white")
        text_stand = font.render("STAND", True, "white")
        text_next = font.render("NEXT", True, "white")

        text_player_points = font.render(f"PLAYER POINTS:{self.player.hand_value()}", True, "white")
        text_dealer_points = font.render(f"DEALER POINTS:{self.dealer.hand_value()}", True, "white")


        # Creates the rect where text is located
        text_hit_rect = text_hit.get_rect(center= hit_rect.center)
        text_stand_rect = text_stand.get_rect(center= stand_rect.center)
        text_next_rect = text_next.get_rect(center= next_rect.center)
        """TODO actualizar los puntos en update"""
        text_player_points_rect = text_player_points.get_rect(center= TEXT_PLAYER_POINTS_POS)
        text_dealer_points_rect = text_dealer_points.get_rect(center= TEXT_DEALER_POINTS_POS)

        text = [
            (text_hit, text_hit_rect),
            (text_stand, text_stand_rect),
            (text_next, text_next_rect),
            (text_player_points, text_player_points_rect),
            (text_dealer_points, text_dealer_points_rect),
        ]
        return text

    def start_game(self):
        self.dealer.turn = False
        #Sets the hands to 0 and restart the deck
        self.player.hand = []
        self.dealer.hand = []
        self.deck.restart_deck()
        self.deck.shuffle()

        #Makes the first deals
        self.player.deal()
        self.dealer.deal()
        self.player.deal()
        self.dealer.deal_upsidedown()

    def update(self):
        font = pg.font.SysFont(None, 25)
        text_player_points = font.render(f"PLAYER POINTS:{self.player.hand_value()}", True, "white")
        text_dealer_points = font.render(f"DEALER POINTS:{self.dealer.hand_value()}", True, "white")
        text_player_points_rect = text_player_points.get_rect(center=TEXT_PLAYER_POINTS_POS)
        text_dealer_points_rect = text_dealer_points.get_rect(center=TEXT_DEALER_POINTS_POS)
        self.text[3] = (text_player_points, text_player_points_rect)
        self.text[4] = (text_dealer_points, text_dealer_points_rect)

        if self.new_game:
            self.new_game = False
            self.start_game()

        elif self.dealer.turn and self.dealer.ended:
            self.check_winner()
            self.dealer.turn = False
            self.dealer.ended = False

        elif self.dealer.turn and not self.dealer.ended:
            self.dealer.perform_turn()




    def handle_events(self,event):
        # Handle the presses of the mouse
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                #Checks if clicking a button
                for key, rect in self.buttons.items():
                    if rect[0].collidepoint(event.pos):
                        #Cheks what button is clicked

                        if key == "hit_button" and not self.ended:
                            # If hit is clicked
                            self.player.deal()
                            if self.player.is_busted():
                                self.dealer.turn = True
                                self.dealer.draw_time = pg.time.get_ticks()

                        if key == "stand_button" and not self.ended:
                            #if stand is clicked
                            self.dealer.turn = True
                            self.dealer.draw_time = pg.time.get_ticks()

                        if key == "next_button":
                            #if next is clicked
                            """TODO Eliminate the Winner text"""
                            self.eliminate_winner_text()
                            self.ended = False
                            self.new_game = True


    def eliminate_winner_text(self):
        if self.ended:
            del self.text[-1]


    def check_winner(self):
        #Cheks who was the winner
        if self.player.is_busted():
            winner = self.dealer.name
        elif self.dealer.is_busted():
            winner = self.player.name
        elif self.player.hand_value() > self.dealer.hand_value():
            winner = self.player.name
        elif self.player.hand_value() < self.dealer.hand_value():
            winner = self.dealer.name
        else:
            winner = "Draw"

        # Adds the text of winner to the texts
        font = pg.font.SysFont(None, 60)
        if winner == "Draw":
            text_winner = font.render(winner, True, "white", "Black")
        else:
            text_winner= font.render(f"{winner} wins!!!", True, "white", "Black")

        text_winner_rect = text_winner.get_rect(center=(SCREEN_CENTER[0], SCREEN_CENTER[1]- 60))
        self.text.append((text_winner, text_winner_rect))
        self.ended = True

