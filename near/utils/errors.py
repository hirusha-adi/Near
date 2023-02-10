class IllegalInput(Exception):
    def __init__(self, message:str=None):
        self.message = message
    
    def __str__(self):
        return f"Illegal Input Passed to the bot as an argument{': ' + str(self.message) if not(self.message is None) else '.'}"
    
    
try:
    raise IllegalInput
except Exception as e:
    print(e)