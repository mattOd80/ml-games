"""
BaseGame Class:

Reason for Being:
- The BaseGame class acts as a foundational blueprint for all games within the system.
- It ensures a consistent structure, interface, and set of functionalities that every game can inherit and build upon.

Use:
- Provides a standardized set of methods and attributes for game lifecycle management, from initialization to completion.
- Manages interactions with the various engines (Rule, Physics, Visualization, Training) in a uniform manner.
- Facilitates data management by providing standardized methods for collecting, storing, and retrieving game data.

Fit into the System:
- All games within the system should inherit from BaseGame to ensure uniformity and compatibility.
- By ensuring a consistent interface and flow, BaseGame simplifies the process of adding new games or modifying existing ones.

Note: Developers creating new games should extend this class and override or add methods as needed to customize the game's specific functionalities.
"""
from shared.shared_components import SharedRules, SharedActions, SharedPhysics

class BaseGame:
    def __init__(self):
        self.game_state = self.initialize_state()
        self.game_rules = self.define_rules()
        self.game_assets = self.load_assets()
        self.game_history = []

    def initialize_state(self):
        # Set up the initial game state
        pass

    def define_rules(self):
        # Define game-specific rules or conditions
        pass

    def load_assets(self):
        # Load necessary game assets
        pass

    def update_state(self, user_input):
        # Use shared rules to determine available moves
        available_moves = SharedRules.available_moves(self.game_state)
        
        # Use shared actions to place a symbol based on user input
        x, y, symbol = user_input  # Assuming user_input is a tuple
        SharedActions.place_symbol(self.game_state, x, y, symbol)
        
        # Use shared physics to apply gravity effect if applicable
        SharedPhysics.gravity_effect(self.game_state, symbol)
        
        # Record the new state and move in game_history
        self.game_history.append((self.game_state.copy(), user_input))

    def render(self):
        # Display the current game state visually
        pass

    def reset(self):
        # Reset the game to its initial state
        self.game_history.clear()

    def get_training_data(self):
        # Extract and format game_history for training purposes
        return self.game_history
