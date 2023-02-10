import re

privilege_escalation_keywords = ['sudo', 'root', 'admin']
privilege_escalation_characters = ['$'] # '!'

def check_input(input_str):
    for keyword in privilege_escalation_keywords:
        if keyword in input_str:
            return False
    
    for character in privilege_escalation_characters:
        if re.search(character, input_str):
            return False
    
    return True


def is_base64(input_str):
    # https://stackoverflow.com/questions/475074/regex-to-parse-or-validate-base64-data
    pattern = r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'
    return re.match(pattern, input_str) is not None
