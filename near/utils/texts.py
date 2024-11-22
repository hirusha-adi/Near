import platform
import pocketbase
from datetime import datetime

import discord


def welcome_message():
    """
    Display a welcome message with ASCII art and system information.
    """
    
    # ASCII art logo
    print(r"""
888b    |                            888~~\             d8   
|Y88b   |  e88~~8e    /~~~8e  888-~\ 888   |  e88~-_  _d88__ 
| Y88b  | d888  88b       88b 888    888 _/  d888   i  888   
|  Y88b | 8888__888  e88~-888 888    888  \  8888   |  888   
|   Y88b| Y888    , C888  888 888    888   | Y888   '  888   
|    Y888  "88___/   "88_-888 888    888__/   "88_-~   "88_/ 
                                                             """)

    # System and environment details
    print(f"""
------------------------------------------------------------
        Date/Time: {datetime.now()}
        Platform: {platform.platform()}
        Node: {platform.uname().node}
        Machine: {platform.uname().machine}
        Python Version: {platform.python_version()}
        Discord.py API Version: {discord.__version__}
        Pocketbase SDK Version: {pocketbase.__version__}
------------------------------------------------------------
                   Made by @hirushaadi
""")
