class SharedRules:
    @staticmethod
    def check_for_line(state_matrix, length, player_symbol):
        """
        Checks for a straight line of a player's symbols.
        
        Parameters:
        - state_matrix (list of lists): The current game state represented as a matrix.
        - length (int): The length of the line to check for.
        - player_symbol (str): The symbol of the player (e.g., 'X' or 'O').
        
        Returns:
        - bool: True if a line of the specified length with the player's symbol is found, False otherwise.
        """
        pass
    
    @staticmethod
    def available_moves(state_matrix):
        """
        Determines the available moves in the current state of the game.
        
        Parameters:
        - state_matrix (list of lists): The current game state represented as a matrix.
        
        Returns:
        - list of tuples: A list of available moves as (x, y) coordinates.
        """
        pass

class SharedActions:
    @staticmethod
    def place_symbol(state_matrix, x, y, symbol):
        """
        Places a player's symbol at a specified location on the game grid.
        
        Parameters:
        - state_matrix (list of lists): The current game state represented as a matrix.
        - x (int): The x-coordinate where the symbol should be placed.
        - y (int): The y-coordinate where the symbol should be placed.
        - symbol (str): The symbol of the player (e.g., 'X' or 'O').
        
        Returns:
        - bool: True if the symbol was placed successfully, False otherwise.
        
        Raises:
        - ValueError: If the specified position is already occupied or out-of-bounds.
        """
        if x < 0 or x >= len(state_matrix) or y < 0 or y >= len(state_matrix[0]):
            raise ValueError("Position out-of-bounds.")
        
        if state_matrix[x][y] is not None:
            raise ValueError("Position already occupied.")
        
        state_matrix[x][y] = symbol
        return True

class SharedPhysics:
    @staticmethod
    def gravity_effect(state_matrix, symbol):
        """
        Simulates the effect of gravity on a player's symbol, making it drop to the lowest available position.
        
        Parameters:
        - state_matrix (list of lists): The current game state represented as a matrix.
        - symbol (str): The symbol of the player (e.g., 'X' or 'O').
        
        Returns:
        - tuple: The final (x, y) position where the symbol settled.
        """
        pass
