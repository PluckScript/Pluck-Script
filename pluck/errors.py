class PluckError(Exception):
    def __init__(self, message, line=None, column=None):
        super().__init__(message)
        self.message = message
        self.line = line
        self.column = column

    def __str__(self):
        loc = f" line: {self.line}, column: {self.column}" if self.line is not None and self.column is not None else ""
        return f"Error: {self.message}{loc}"

class returnException(Exception):
    def __init__(self, value):
        self.value = value

class breakException(Exception):
    pass