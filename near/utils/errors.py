def handle_command_errors(func):
    # TO BE COMPLETED LATER
    ...


class IllegalInput(Exception):
    """
    Exception raised for illegal input passed to commands.
    """

    def __init__(self, message: str = None):
        self.message = message

    def __str__(self):
        return f"Illegal Input Passed to the bot as an argument{': ' + str(self.message) if not(self.message is None) else '.'}"


class CommandError(Exception):
    """
    Exception raised for errors while running a command.
    """

    def __init__(self, message: str = None):
        self.message = message

    def __str__(self):
        return self.message or "Unable to run the command"


class PermissionError(Exception):
    """
    Exception raised for lack of permissions to run the command.
    """

    def __init__(self, message: str = None):
        self.message = message

    def __str__(self):
        return self.message or "You do not have enough permissions to run this command!"  

class PocketBaseError(Exception):
    """
    Exception raised for an issue related to PocketBase.
    """

    def __init__(self, message: str = None):
        self.message = message

    def __str__(self):
        return self.message or "An error occured with pocketbase/database."  
