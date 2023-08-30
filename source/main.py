# Import necessary modules and dependencies
from engines.rule_engine import RuleEngine
from engines.physics_engine import PhysicsEngine
from engines.visualization_engine import VisualizationEngine
from engines.training_engine import TrainingEngine
import argparse
import importlib

from games.debug_game import DebugGame


class Main:

    def __init__(self):
        # Initialize the game and engine instances
        self.game = None
        self.rule_engine = RuleEngine()
        self.physics_engine = PhysicsEngine()
        self.visualization_engine = VisualizationEngine()
        self.training_engine = TrainingEngine()

    def load_game(self, game_name: str):
        try:
            module_name = ''.join(['_' + i.lower() if i.isupper() else i for i in game_name]).lstrip('_')
            print(f"Trying to load module: games.{module_name}")  # Debug print
            game_module = importlib.import_module(f"games.{module_name}")
            print(f"Trying to instantiate class: {game_name}")  # Debug print
            self.game = getattr(game_module, game_name)()
        except (ModuleNotFoundError, AttributeError) as e:
            print(f"Debug Error: {e}")  # Print the actual error for debugging
            raise ValueError(f"Unknown game: {game_name}.")

    def main(self):
        # Core gameplay loop
        while True:
            # 1. Evaluate game state with the rule engine
            self.rule_engine.evaluate(self.game.game_state)

            # 2. Simulate physics
            self.physics_engine.apply_physics(self.game.game_state)

            # 3. Render visuals
            self.visualization_engine.render(self.game.game_state)

            # 4. Collect and process data
            raw_data = self.training_engine.collect_data(self.game.game_state)
            processed_data = self.training_engine.process_data(raw_data)

            # TODO: Add game logic, user input, and other necessary interactions.

            # Exit condition for the loop. This will be replaced by actual game conditions.
            break

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Load a specific game.")
    parser.add_argument("--game", type=str, help="Name of the game to load.")
    args = parser.parse_args()

    main_app = Main()

    if args.game:
        game_to_load = args.game
    else:
        game_to_load = input("Enter the name of the game to load: ")

    try:
        main_app.load_game(game_to_load)
        main_app.main()
    except Exception as e:
        print(f"Error: {e}")
