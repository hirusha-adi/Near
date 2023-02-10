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




