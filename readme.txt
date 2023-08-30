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
## Tracking & Reporting Snapshot Context
1. Continuously monitor code changes shared by the human developer and update 'llm_snapshot_context.txt' accordingly.
2. Compare with existing Snapshot Context.
3. If discrepancies are found, report to the human developer:

'''
Suggested Snapshot Context Update for [FILENAME]:
Date: [YYYY-MM-DD]
Status: [Suggested Status]
Key Functions/Methods: [Updated Functions/Methods]
Primary Dependencies: [Updated Dependencies]
TODO: [New Tasks]
Reminder: [Important Notes]
Collaboration Tips
Always request the latest version of the file from the human developer before analysis.
Provide clear and concise feedback.
Prioritize updates to the Snapshot Context for clarity and consistency.
Note: LLM's primary role is to assist, analyze, and report. Direct changes are executed by the human developer.
'''

Note: Always refer to 'llm_snapshot_context.txt' for the latest context. This file should be the primary source of truth for the project's current state and updates.
