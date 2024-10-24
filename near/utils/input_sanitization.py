import re

privilege_escalation_keywords = ['sudo', 'root', 'admin']

def check_input(input_str: str) -> bool:
    """
    Check if input string contains any potentially harmful commands.

    Args:
        input_str: The string to check.

    Returns:
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
        input_str: The string to check.

    Returns:
        True if the string is a valid base64 string,
        False if it is not.
    """

    pattern = r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'
    return re.match(pattern, input_str) is not None


def is_ipaddr(input_str: str) -> bool:
    """
    Check if input string is a valid IP address (both IPv4 and IPv6).
    Based on:
        IPv4: https://stackoverflow.com/questions/5284147/validating-ipv4-addresses-with-regexp
        IPv6: https://stackoverflow.com/questions/53497/regular-expression-that-matches-valid-ipv6-addresses

    Args:
        input_str: The string to check.

    Returns:
        True if the string is a valid IP address,
        False if it is not.
    """

    ipv4 = r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    ipv6 = r'(([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6})|:((:[0-9a-fA-F]{1,4}){1,7}|:)|fe80:(:[0-9a-fA-F]{0,4}){0,4}%[0-9a-zA-Z]{1,}|::(ffff(:0{1,4}){0,1}:){0,1}((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])|([0-9a-fA-F]{1,4}:){1,4}:((25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9])\.){3,3}(25[0-5]|(2[0-4]|1{0,1}[0-9]){0,1}[0-9]))'
    return (re.match(ipv4, input_str) or re.match(ipv6, input_str)) is not None


def is_text_only(input_str: str) -> bool:
    """
    Check if the input string contains only alphabetic characters.

    Args:
        input_str: The string to check.

    Returns:
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
        input_str: The string to check.

    Returns:
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
        int: The integer value of the given hex string.
        If the conversion fails, return the default color red (int: 0xFF0000).
    """
    try:
        return int(hex, 16)
    except ValueError:
        return 0xFF0000  # return default color red
