from .game_state import GameState


class StateManager:

    def __init__(self, player, dealer):
        self.actual_state = GameState(player, dealer)
        self.player = player
        self.dealer = dealer

    def draw(self,screen):
        self.actual_state.draw(screen)

    def change_state(self,new_state):
        self.actual_state = new_state

    def update(self):
        self.actual_state.update()

    def handle_events(self, event):
        self.actual_state.handle_events(event)
