from engines.rule_engine import RuleEngine
from engines.physics_engine import PhysicsEngine
from engines.visualization_engine import VisualizeInConsole

class GameOfLife:
    def __init__(self, rule_engine, physics_engine, visualizer=VisualizeInConsole()):
        self.rule_engine = rule_engine
        self.physics_engine = physics_engine
        self.visualizer = visualizer
        self.state_matrix = self.initialize_state()

    # ... (rest of the implementation remains unchanged)

    def start_game(self):
        self.visualizer.display(self.state_matrix)

    def play_turn(self):
        self.state_matrix = self.rule_engine.evolve(self.state_matrix)
        self.visualizer.display(self.state_matrix)
