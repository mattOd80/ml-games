from games.base_game import BaseGame

class DebugGame(BaseGame):
    def __init__(self):
        super().__init__()

    def log_call(self, caller_name, *args, **kwargs):
        """
        Log the caller's name and the passed arguments.
        
        Parameters:
        - caller_name (str): Name of the calling function or method.
        - *args: Positional arguments passed to the caller.
        - **kwargs: Keyword arguments passed to the caller.
        """
        print(f"Caller: {caller_name}")
        print(f"Arguments: {args}")
        if kwargs:
            print(f"Keyword Arguments: {kwargs}")
        print("-" * 40)  # Separator for clarity

    def update_state(self, user_input):
        # Log the call details
        self.log_call("update_state", user_input)
        
        # Update game state based on user input and game rules
        super().update_state(user_input)

    # Override other methods from BaseGame to add logging as needed
