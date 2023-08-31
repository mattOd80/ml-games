from base_game import BaseGame
class TicTacToe(BaseGame):
    def initialize_state(self):
        # Initialize a 3x3 matrix for Tic Tac Toe
        return [['' for _ in range(3)] for _ in range(3)]

    def define_rules(self):
        # Define rules specific to Tic Tac Toe
        pass

    def render(self):
        # Display the Tic Tac Toe grid visually
        pass
