import ipaddress
import re
import typing as t

privilege_escalation_keywords = [
    'sudo', 'root', 'admin', 'polkit', 'pkexec', 'gksudo', 'kdesudo',
    'doas', 'pfexec', 'chroot', 'systemd-run', 'systemd-nspawn', 'docker', 
    # 'su',
]

def check_input(input_str: str) -> bool:
    """
    Check if input string contains any potentially harmful commands.

    Parameters
    ----------
    input_str : str
        The string to check.

    Returns
    -------
    bool
        True if the string is safe, False if it contains a harmful command.
    """
    
    for keyword in privilege_escalation_keywords:
        if keyword in input_str:
            return False
    return True


def is_base64(input_str: str) -> bool:
    """
    Check if input string is a valid base64 string.

    Parameters
    ----------
    input_str : str
        The string to check.

    Returns
    -------
    bool
        True if the string is a valid base64 string,
        False if it is not.
    """

    pattern = r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'
    return re.match(pattern, input_str) is not None


def is_ipaddr(input_str: str) -> bool:
    """
    Check if input string is a valid IP address (both IPv4 and IPv6).

    Parameters
    ----------
    input_str : str
        The string to check.

    Returns
    -------
    bool
        True if the string is a valid IP address, False otherwise.
    """
    
    try:
        ipaddress.ip_address(input_str)
        return True
    except ValueError:
        return False

def is_text_only(input_str: str) -> bool:
    """
    Check if the input string contains only alphabetic characters.

    Parameters
    ----------
    input_str : str
        The string to check.

    Returns
    -------
    bool
        True if the string contains only alphabetic characters,
        False otherwise.
    """

    pattern = r'^[a-zA-Z]+$'
    return re.match(pattern, input_str) is not None


def is_instagram_username(input_str: str) -> bool:
    """
    Check if the input string is a valid Instagram username.

    Valid Instagram usernames:
    - Must be 1-29 characters long
    - Must only contain alphanumeric characters

    Parameters
    ----------
    input_str : str
        The string to check.

    Returns
    -------
    bool
        True if the string is a valid Instagram username,
        False otherwise.
    """

    pattern = r'^[a-zA-Z0-9]{1,29}$'
    return re.match(pattern, input_str) is not None


def password_check(input_str):
    # TODO: complete. or remove this completely.
    # change this later
    return check_input(input_str)


def color(col: t.Union[str, t.Literal["red", "green", "blue", "yellow", "purple", "cyan", "orange"]]) -> int:
    """
    Convert a color string into an integer.

    Parameters
    ----------
    col : str
        The color string. Can be a color name or a hex color string.
        Supported color names: red, green, blue, yellow, purple, cyan, orange

    Returns
    -------
    int
        The color as an integer.
    """
    
    try:
        col = col.lower()
        colors = {
            "red": 0xFF0000,
            "green": 0x00FF00,
            "blue": 0x0000FF,
            "yellow": 0xFFFF00,
            "purple": 0xFF00FF,
            "cyan": 0x00FFFF,
            "orange": 0xFFA500
        }
        return colors.get(
            col, 
            int(col, 16)    # default to converting 
                            # eg: 0xff0000 or ff0000
        )
    except ValueError:
        return 0xFF0000
