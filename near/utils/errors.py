def handle_command_errors(func):
    # TO BE COMPLETED LATER
    ...


class IllegalInput(Exception):
    def __init__(self, message: str = None):
        self.message = message

    def __str__(self):
        return f"Illegal Input Passed to the bot as an argument{': ' + str(self.message) if not(self.message is None) else '.'}"


class CommandError(Exception):
    def __init__(self, message: str = None):
        self.message = message

    def __str__(self):
        return f"Error running the command{': ' + str(self.message) if not(self.message is None) else '.'}"
