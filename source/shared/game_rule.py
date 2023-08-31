'''
Rule Type Support Goals:

The system aims to support a diverse set of rule types to cater to various game scenarios and simulations. The following table outlines potential rule types, their characteristics, and their compatibility with different stage types:

| Stage Type            | Rule Type               | Description                                                                 | Typical Use Case                                     | Example Games/Scenarios      | Notes & Special Characteristics |
|-----------------------|-------------------------|-----------------------------------------------------------------------------|------------------------------------------------------|-----------------------------|--------------------------------|
| 2D Grid               | Boundary Check          | Validates if a move/action is within the grid boundaries.                   | Traditional board games                              | Tic Tac Toe, Chess          | Regular grid, fixed size      |
| 2D Grid               | Win Condition Check     | Checks for conditions that determine a win.                                 | Traditional board games                              | Tic Tac Toe, Connect Four   | Varies based on game rules    |
| 3D Grid               | 3D Boundary Check       | Validates if a move/action is within the 3D grid boundaries.                | 3D board games                                       | 3D Tic Tac Toe              | Regular 3D grid, fixed size  |
| Dictionary Grid       | Key Existence Check     | Validates if a key exists in the dictionary.                                | Games with sparse data                               | Some roguelikes             | Key-value pairs, dynamic size |
| Graph                 | Node Connectivity Check | Validates if two nodes are connected.                                       | Network-based games                                  | Social network games        | Nodes and edges              |
| Continuous 2D Surface | Value Range Check       | Validates if a value is within a specified range.                           | Physics simulations                                  | Water flow simulations      | Continuous values            |
| Continuous 3D Space   | 3D Value Range Check    | Validates if a 3D value is within a specified range.                        | 3D simulations                                       | Space exploration games     | Continuous values in 3D      |

For version 1 (v1), the system will prioritize support for the following rule types:

1. **Boundary Check**:
   - **Stage Type**: 2D Grid
   - **Description**: Validates if a move/action is within the grid boundaries.
   - **Typical Use Case**: Traditional board games
   - **Example Games/Scenarios**: Tic Tac Toe, Chess
   - **Notes & Special Characteristics**: Regular grid, fixed size

2. **Win Condition Check**:
   - **Stage Type**: 2D Grid
   - **Description**: Checks for conditions that determine a win.
   - **Typical Use Case**: Traditional board games
   - **Example Games/Scenarios**: Tic Tac Toe, Connect Four
   - **Notes & Special Characteristics**: Varies based on game rules

... [and so on for each rule type prioritized for v1]

These rule types will form the foundation for the system's capabilities in v1, with plans to expand support for additional rule types in future versions.


# Current discussion on the subject of RuleTypes (or game rules or whatever they get called)

| Stage Type            | Rule Type               | Description                                                                 | Typical Use Case                                     | Example Games/Scenarios      | Notes & Special Characteristics |
|-----------------------|-------------------------|-----------------------------------------------------------------------------|------------------------------------------------------|-----------------------------|--------------------------------|
| 2D Grid               | Grid Boundary Check     | Validates if a move/action is within the grid boundaries.                   | Traditional board games                              | Tic Tac Toe, Chess          | Regular grid, fixed size      |
| 2D Grid               | Line Formation Check    | Checks for a straight line of symbols.                                      | Traditional board games                              | Tic Tac Toe, Connect Four   | Varies based on game rules    |
| 3D Grid               | Volume Boundary Check   | Validates if a move/action is within the 3D grid boundaries.                | 3D board games                                       | 3D Tic Tac Toe              | Regular 3D grid, fixed size  |
| Dictionary Grid       | Key-Value Validation    | Validates if a key-value pair meets certain criteria.                       | Games with sparse data                               | Some roguelikes             | Key-value pairs, dynamic size |
| Graph                 | Connectivity Check      | Validates if two nodes are connected.                                       | Network-based games                                  | Social network games        | Nodes and edges              |
| Continuous 2D Surface | Surface Value Range     | Validates if a value is within a specified range on the surface.            | Physics simulations                                  | Water flow simulations      | Continuous values            |
| Continuous 3D Space   | Space Boundary Check    | Validates if a position is within a defined 3D space.                       | 3D simulations                                       | Space exploration games     | Continuous values in 3D      |
| All                   | Turn-Based Validation   | Ensures actions/moves adhere to turn-based mechanics.                       | Turn-based games                                     | Chess, Turn-based RPGs      | Sequential player actions    |
| All                   | Resource Limit Check    | Validates if actions/moves are within resource limits (e.g., mana, energy). | Resource-constrained games                           | Strategy games, RPGs        | Resource management          |
| All                   | Cooldown Check          | Ensures actions/moves respect cooldown periods.                             | Real-time games with action/move cooldowns           | MOBAs, Action RPGs          | Time-based action limits     |

| Stage Type            | Rule Type 1              | Rule Type 2                | Rule Type 3                  |
|-----------------------|--------------------------|----------------------------|-----------------------------|
| 2D Grid               | Grid Boundary Check      | Line Formation Check       | Turn-Based Validation       |
| 3D Grid               | Volume Boundary Check    | 3D Object Interaction      | Gravity Effect Validation   |
| Dictionary Grid       | Key-Value Validation     | Dynamic Size Check         | Data Integrity Check        |
| Graph                 | Connectivity Check       | Node Existence Validation  | Edge Weight Validation      |
| Continuous 2D Surface | Surface Value Range      | Fluid Dynamics Check       | Surface Interaction Check   |
| Continuous 3D Space   | Space Boundary Check     | Object Collision Check     | 3D Movement Validation      |
| Multi-dimensional     | Dimensional Boundary     | Data Point Validation      | Multi-D Interaction Check   |
| Geographical          | Geographic Boundary Check| Layer Interaction Check    | Real-world Data Validation  |
| Hypersurface          | Surface Integrity Check  | Mathematical Validation    | Hyperspace Interaction      |
| Dynamic Network       | Node Evolution Check     | Dynamic Connectivity Check | Network Integrity Validation|
'''
