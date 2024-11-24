import typing as t
from loguru import logger

from near.database import dbfetch


async def log_command_history(
    command: str, 
    author_id: str, 
    author_name: str, 
    command_args: t.Optional[str] = "", 
    server_id: t.Optional[str] = "", 
    server_name: t.Optional[str] = ""
) -> None:
    """
    Logs the execution of a command to both the console and PocketBase.

    Parameters
    ----------
    command : str
        The command that was executed.
    author_id : str
        The ID of the user who executed the command.
    author_name : str
        The name of the user who executed the command.
    command_args : Optional[str], optional
        Additional arguments for the command, by default "".
    server_id : Optional[str], optional
        The ID of the server where the command was executed, by default "".
    server_name : Optional[str], optional
        The name of the server where the command was executed, by default "".
    """
    
    # default stdout to console
    logger.info(f"Command invoked by {author_name} ({author_id}) in {server_name} ({server_id}): {command} {command_args}")
    
    # log to pocketbase
    dbfetch.CommandsHistory.createOneRec(
        command=command, 
        command_args=command_args, 
        author_id=author_id, 
        author_name=author_name, 
        server_id=server_id, 
        server_name=server_name
    )
