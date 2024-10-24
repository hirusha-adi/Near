import ipaddress
import re

privilege_escalation_keywords = [
    'sudo', 'root', 'admin', 'polkit', 'pkexec', 'gksudo', 'kdesudo',
    'doas', 'pfexec', 'chroot', 'systemd-run', 'systemd-nspawn', 'docker', 
    # 'su',
]

def check_input(input_str: str) -> bool:
    """
    Check if input string contains any potentially harmful commands.

    Args:
        input_str (str): The string to check.

    Returns:
        bool: 
            True if the string is safe, 
            False if it contains a harmful command.
    """
    
    for keyword in privilege_escalation_keywords:
        if keyword in input_str:
            return False
    return True


def is_base64(input_str: str) -> bool:
    """
    Check if input string is a valid base64 string.
    Based on: https://stackoverflow.com/questions/475074/regex-to-parse-or-validate-base64-data

    Args:
        input_str (str): The string to check.

    Returns:
        bool: 
            True if the string is a valid base64 string,
            False if it is not.
    """

    pattern = r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'
    return re.match(pattern, input_str) is not None


def is_ipaddr(input_str: str) -> bool:
    """
    Checks if input string is a valid IP address (both IPv4 and IPv6).
    Based on: 
        https://gist.github.com/hirusha-adi/5ed5000246e16dfa035ea604362c763f
        https://docs.python.org/3/library/ipaddress.html#ipaddress.ip_address

    Args:
        input_str (str): The string to check.

    Returns:
        bool: 
            True if the string is a valid IP address, 
            False otherwise.
    """
    try:
        ipaddress.ip_address(input_str)
        return True
    except ValueError:
        return False

def is_text_only(input_str: str) -> bool:
    """
    Check if the input string contains only alphabetic characters.

    Args:
        input_str (str): The string to check.

    Returns:
        bool: 
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

    Args:
        input_str (str): The string to check.

    Returns:
        bool: 
            True if the string is a valid Instagram username,
            False otherwise.
    """

    pattern = r'^[a-zA-Z0-9]{1,29}$'
    return re.match(pattern, input_str) is not None


def password_check(input_str):
    # TODO: complete. or remove this completely.
    # change this later
    return check_input(input_str)


def color(hex: str) -> int:
    """
    Convert a given hex string to an integer.

    Args:
        hex (str): The string to convert.

    Returns:
        int: 
            The integer value of the given hex string.
            If the conversion fails, return the default color red (int: 0xFF0000).
    """
    try:
        return int(hex, 16)
    except ValueError:
        return 0xFF0000  # return default color red
