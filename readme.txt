A modular game/simulation system developed in Python. Provides dynamic game play with various engine integrations.
Key Features:
- Multiple engines (rule, physics, visualization, data storage)
- CNN training interface
- Modular design: Easily switch or tweak games/engines

Sure, here's a condensed and information-dense overview of your project:

---

### Project Overview: Dynamic Game/Simulation System

**Objective:** Develop a comprehensive framework facilitating the dynamic execution, visualization, and data collection of games and simulations with a strong focus on modularity, interchangeability, and extensibility.

#### Key Goals:

1. **Dynamic Loading:** Enable on-the-fly loading and execution of diverse game or simulation modules.
  
2. **Engine Integration:**
   - **Rule Engine:** Implement and manage game-specific rules.
   - **Physics Engine:** Drive accurate simulations of physical interactions.
   - **Visualization Engine:** Provide representations ranging from console outputs to immersive 3D visuals.
   - **Data Storage Engine:** Efficiently store, retrieve, and manage gameplay data.
   - **Training Engine:** Interface for Convolutional Neural Network (CNN) training on gameplay data.

3. **Gameplay Modes:** Support both human-driven and automated gameplay experiences.

4. **Modularity & Interchangeability:** Design system components to be easily swapped out or adjusted without disrupting the entire framework.

5. **Interoperability:** Ensure seamless communication between engines, particularly in passing data and recognizing shared data structures.

#### Technical Blueprint:

- **Setup:** Python 3.8+ environment with dependencies managed via `requirements.txt`.
  
- **Core Architecture:** 
   - Central orchestration through `main.py`.
   - Engines are compartmentalized within the `engines/` directory, each offering specific functionalities (rule evaluation, physics simulation, visualization, and data collection for CNN training).
   - Shared utilities like rules and moves are housed within the `shared/` directory.
   - Game templates and instances reside in the `games/` directory, leveraging the base game structure from `base_game.py`.

- **Data Flow & Interoperability:** 
   - Centralized game state acting as the universal language between engines.
   - Bidirectional data flow designed between the main script, game instances, and engines.
   - Modular design mandates adherence to common data structures (game state, rules, moves) for seamless engine interop.

#### Implementation Guidance:

1. Utilize the "Snapshot Context" and "Current Context" documentation strategies for every file, ensuring continuity and instant recall of a file's current status and details.
  
2. Keep interoperability in focus. As engines evolve or new ones are introduced, adherence to shared data structures is crucial.
  
3. Regularly update the core README to reflect any major changes or shifts in project direction, keeping it as the single source of truth.

---

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

Branching Strategy:
- At session start, LLM checks 'llm_snapshot_context.txt' for branch status.
- For ongoing sessions, LLM continues with the specified branch.
- For new sessions, LLM suggests a branch name based on the session topic.
