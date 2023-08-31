'''
Stage Type Support Goals:

The system aims to support a broad range of stage types to cater to diverse game scenarios and simulations. The following table outlines the potential stage types and their characteristics:

| Stage Type Name       | Dimensions | Data Structure | Typical Use Case                          | Example Games/Scenarios                   | Notes & Special Characteristics |
|-----------------------|------------|----------------|-------------------------------------------|------------------------------------------|--------------------------------|
| 2D Grid               | 2D         | Array of Arrays| Traditional board games                   | Tic Tac Toe, Chess                       | Regular grid, fixed size      |
| 3D Grid               | 3D         | 3D Array       | 3D board games, voxel-based games        | 3D Tic Tac Toe, Minecraft-like games     | Regular 3D grid, fixed size  |
| Dictionary Grid       | 2D         | Dictionary     | Games with sparse data                    | Some roguelikes                          | Key-value pairs, dynamic size |
| Graph                 | N/A        | Graph          | Network-based games                       | Social network games                     | Nodes and edges              |
| Continuous 2D Surface | 2D         | Matrix         | Physics simulations, fluid dynamics      | Water flow simulations                   | Continuous values            |
| Continuous 3D Space   | 3D         | 3D Matrix      | 3D simulations, space games               | Space exploration games                  | Continuous values in 3D      |
| Multi-dimensional     | >3D        | Multi-D Array  | Hypothetical spaces, data-rich scenarios | Data visualizations, AI training spaces  | Multiple dimensions          |
| Geographical          | 2D/3D      | GIS Data       | Real-world mapping, strategy games       | Civilization, SimCity                    | Real-world data, layers      |
| Hypersurface          | >3D        | Complex Array  | Advanced mathematical simulations        | Hyperspace travel simulations            | Mathematical representation  |
| Dynamic Network       | N/A        | Dynamic Graph  | Evolving network games                    | Evolutionary games, neural network games | Nodes, edges change over time|


For version 1 (v1), the system will prioritize support for the following stage types:

1. **2D Grid**:
   - **Dimensions**: 2D
   - **Data Structure**: Array of Arrays
   - **Typical Use Case**: Traditional board games
   - **Example Games/Scenarios**: Tic Tac Toe, Chess
   - **Notes & Special Characteristics**: Regular grid, fixed size

2. **3D Grid**:
   - **Dimensions**: 3D
   - **Data Structure**: 3D Array
   - **Typical Use Case**: 3D board games, voxel-based games
   - **Example Games/Scenarios**: 3D Tic Tac Toe, Minecraft-like games
   - **Notes & Special Characteristics**: Regular 3D grid, fixed size

3. **Dictionary Grid**:
   - **Dimensions**: 2D
   - **Data Structure**: Dictionary
   - **Typical Use Case**: Games with sparse data
   - **Example Games/Scenarios**: Some roguelikes
   - **Notes & Special Characteristics**: Key-value pairs, dynamic size

4. **Graph**:
   - **Dimensions**: N/A
   - **Data Structure**: Graph
   - **Typical Use Case**: Network-based games
   - **Example Games/Scenarios**: Social network games
   - **Notes & Special Characteristics**: Nodes and edges

5. **Continuous 2D Surface**:
   - **Dimensions**: 2D
   - **Data Structure**: Matrix
   - **Typical Use Case**: Physics simulations, fluid dynamics
   - **Example Games/Scenarios**: Water flow simulations
   - **Notes & Special Characteristics**: Continuous values

6. **Continuous 3D Space**:
   - **Dimensions**: 3D
   - **Data Structure**: 3D Matrix
   - **Typical Use Case**: 3D simulations, space games
   - **Example Games/Scenarios**: Space exploration games
   - **Notes & Special Characteristics**: Continuous values in 3D

These stage types will form the foundation for the system's capabilities in v1, with plans to expand support for additional stage types in future versions.


'''
from enum import Enum, auto

class StageType(Enum):
    GRID_2D = auto()
    GRID_3D = auto()
    DICTIONARY_GRID = auto()
    GRAPH = auto()
    CONTINUOUS_2D_SURFACE = auto()
    CONTINUOUS_3D_SPACE = auto()
