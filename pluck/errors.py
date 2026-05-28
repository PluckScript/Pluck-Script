class PluckError():
    pass

class returnException(Exception):
    def __init__(self, value):
        self.value = value

class breakException(Exception):
    pass