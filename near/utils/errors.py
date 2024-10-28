def handle_command_errors(func):
    # TO BE COMPLETED LATER
    ...


class IllegalInput(Exception):
    """
    Exception raised for illegal input passed to commands.

    Parameters
    ----------
    message : str
        The message to be displayed with the error. If not provided, a default
        message will be used.

    Attributes
    ----------
    message : str
        The message to be displayed with the error.

    Notes
    -----
    This exception is raised when the input provided to a command is not valid.
    """

    def __init__(self, message: str = None):
        """
        Initialize the IllegalInput exception.

        Parameters
        ----------
        message : str
            The message to be displayed with the error. If not provided, a default
            message will be used.
        """
        self.message = message

    def __str__(self):
        """
        Return a string representation of the exception.

        Returns
        -------
        str
            A string representation of the exception.
        """
        return f"Illegal Input Passed to the bot as an argument{': ' + str(self.message) if not(self.message is None) else '.'}"


class CommandError(Exception):
    """
    Exception raised for errors while running a command.

    Parameters
    ----------
    message : str, optional
        The message to be displayed with the error. If not provided, a default
        message will be used.

    Attributes
    ----------
    message : str
        The message to be displayed with the error.

    Notes
    -----
    This exception is raised when the command itself is unable to run due to
    some error.
    """

    def __init__(self, message: str = None):
        """
        Initialize the CommandError exception.

        Parameters
        ----------
        message : str, optional
            The message to be displayed with the error. If not provided, a default
            message will be used.
        """
        self.message = message

    def __str__(self):
        """
        Return a string representation of the exception.

        Returns
        -------
        str
            A string representation of the exception.
        """
        return self.message or "Unable to run the command"
