A modular game/simulation system developed in Python. Provides dynamic game play with various engine integrations.
Key Features:
- Multiple engines (rule, physics, visualization, data storage)
- CNN training interface
- Modular design: Easily switch or tweak games/engines
Project Structure with Export Details:
--------
/
    |- readme.txt
    # this documentation

    |- source/
        |- main.py 
           # Central orchestration.
           # Methods:
           # - load_game(game_name: str): Dynamically loads a game.
           # - main(): Core gameplay loop.

        |- engines/                   
        |   |- rule_engine.py         
        |      # Rule Engine.
        |      # Exported Class: RuleEngine
        |      #     - evaluate(game_state: object): Evaluates game rules.

        |   |- physics_engine.py      
        |      # Physics Engine.
        |      # Exported Class: PhysicsEngine
        |      #     - simulate(game_state: object): Simulates physics.

        |   |- visualization_engine.py
        |      # Visualization Engine.
        |      # Exported Class: VisualizationEngine
        |      #     - render(game_state: object): Renders visuals.

        |   |- training_engine.py     
        |      # Training Engine.
        |      # Exported Class: TrainingEngine
        |      #     - collect_data(game_state: object): Data collection.
        |      #     - process_data(raw_data: object): Processes data.

        |- shared/
        |   |- rules.py
        |      # Shared Rules.
        |      # Exported Class: Rule

        |   |- moves.py
        |      # Shared Moves.
        |      # Exported Class: Move

        |- games/                     
        |   |- base_game.py        
        |      # Base Game.
        |      # Exported Class: BaseGame















-------------------------------
    INTEROPERABILITY & DATA FLOW
-------------------------------

The modular game/simulation system is developed in Python and is designed to provide seamless interoperability across various engines and components.

1. **Game State Consistency**:
    - All engines (rule, physics, visualization, and data storage) use a consistent game state format provided by the game instance.
    - This consistency ensures that there's no loss of data or misinterpretation when the game state travels between different engines.

2. **Main Orchestrator**:
    - The `main.py` serves as the central orchestrator. It leverages the game instance and the engines to conduct gameplay.
    - Data flow is designed as: Main -> Game -> Engines, but it allows bi-directional flow. This ensures that the engines can modify the game state and send it back to the game instance if needed.

3. **User Interactions & Controls**:
    - User input is fetched in the main gameplay loop and is used to update the game state or control game flow.
    - Ensure that any game or engine that gets integrated has clear mechanisms to handle and interpret user input, making the integration process smooth.

4. **Engine Interactions**:
    - The Rule Engine evaluates the current game state to check for rule-specific scenarios or game conditions.
    - The Physics Engine simulates physics based on the game state.
    - The Visualization Engine renders visuals based on the game state.
    - The Training Engine can collect and process data using the current game state.

5. **Dynamic Game Loading**:
    - The system is designed to dynamically load games. The `load_game` method in `main.py` facilitates this. It's essential to ensure that any new game added to the system adheres to the required game state format and provides necessary methods to interact with the engines.

6. **Recommendation for Developers**:
    - While integrating new engines or games, always run tests individually for each component to ensure they work correctly in isolation before full integration.


Updating File's "Snapshot" Context:
-----------------------------------
At the top of each file, maintain a concise "Snapshot Context". This brief section should be updated each time the file is saved to provide an immediate understanding of the file's current state. It serves as a "quick glance" guide before diving deeper into the file or the more detailed Current Context template.

Snapshot Context Template:
'''
    Snapshot Context: [FILENAME]
    Date: [YYYY-MM-DD]
    Status: [Complete/In-Progress/Pending]
    Key Functions/Methods: [Function1, Function2, ...]
    Primary Dependencies: [Module1, Module2, ...]
    TODO: [Brief task or change description.]
    Reminder: [One-line important note.]
'''

Instructions:
    Filename: Clearly mention the filename for clarity.
    Date: Always keep the date updated to the latest save.
    Status: In one word, mention the development status of the file.
    Key Functions/Methods: List the primary functions or methods in the file.
    Primary Dependencies: Mention main dependencies or modules the file relies upon.
    TODO: A very brief description of what needs to be done next.

Reminder: Any critical, one-line note that needs immediate attention.