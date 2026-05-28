from pluck.tokens import *
from pluck.errors import *

class Lexer:

    def __init__(self, text):

        self.text = text
        self.position = 0
        self.line = 1
        self.column = 1

        if len(text) > 0:
            self.current_char = text[self.position]
        else:
            self.current_char = None

    def advance(self):

        if self.current_char == "\n":
            self.line += 1
            self.column = 1
        else:
            self.column += 1

        self.position += 1

        if self.position >= len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.position]

    def peek(self):
        if self.position + 1 >= len(self.text):
            return None
        return self.text[self.position + 1]

    def skip_whitespace(self):

        while self.current_char is not None and self.current_char in " \t":
            self.advance()

    def number(self):
        result = ""
        has_dot = False
        while self.current_char is not None and (self.current_char.isdigit()):
            result += self.current_char
            self.advance()
        if has_dot:
            return Token(FLOAT, float(result), self.line, self.column)
        else:
            return Token(NUMBER, int(result), self.line, self.column)

    def string(self):

        self.advance()

        result = ""

        while self.current_char is not None and self.current_char != '"':

            result += self.current_char
            self.advance()

        self.advance()

        return Token(STRING, result, self.line, self.column)

    def boolean(self):

        result = ""

        while self.current_char is not None and self.current_char.isalpha():

            result += self.current_char
            self.advance()

        if result == "true":
            return Token(TRUE, True, self.line, self.column)
        elif result == "false":
            return Token(FALSE, False, self.line, self.column)
        else:
            raise Exception(f"Invalid boolean literal: {result}")
        
    def identifier(self):

        result = ""

        while self.current_char is not None and (
            self.current_char.isalnum() or self.current_char == "_"
        ):

            result += self.current_char
            self.advance()

        KEYWORDS = {
            "if": IF,
            "elif": ELIF,
            "else": ELSE,
            "while": WHILE,
            "for": FOR,
            "fn": FN,
            "true": TRUE,
            "false": FALSE,
            "return": RETURN,
            "break": BREAK,
            "import": IMPORT,
        }

        if result in KEYWORDS:
            return Token(KEYWORDS[result], self.line, self.column)

        return Token(IDENTIFIER, result, self.line, self.column)

    def get_next_token(self):
        try:
            while self.current_char is not None:

                if self.current_char == "\n":
                    self.advance()
                    return Token(NEWLINE, self.line, self.column)

                if self.current_char in " \t":
                    self.skip_whitespace()
                    continue

                if self.current_char.isdigit():
                    return self.number()

                if self.current_char == '"':
                    return self.string()

                if self.current_char.isalpha():
                    return self.identifier()

                if self.current_char == "+":
                    self.advance()
                    return Token(PLUS, self.line, self.column)

                if self.current_char == "-":
                    self.advance()
                    return Token(MINUS, self.line, self.column)

                if self.current_char == "*":
                    self.advance()
                    if self.current_char == "*":
                        self.advance()
                        return Token(EXPONENT, self.line, self.column)
                    return Token(MULTIPLY, self.line, self.column)

                if self.current_char == "/":
                    self.advance()
                    if self.current_char == "/":
                        while self.current_char is not None and self.current_char != "\n":
                            self.advance()
                        continue
                    else:
                        return Token(DIVIDE, self.line, self.column)

                if self.current_char == "%":
                    self.advance()
                    return Token(MODULO, self.line, self.column)

                if self.current_char == "(":
                    self.advance()
                    return Token(LPAREN, self.line, self.column)

                if self.current_char == ")":
                    self.advance()
                    return Token(RPAREN, self.line, self.column)

                if self.current_char == "=":
                    self.advance()
                    return Token(EQUALS, self.line, self.column)

                if self.current_char == ",":
                    self.advance()
                    return Token(COMMA, self.line, self.column)

                if self.current_char == ">":
                    self.advance()
                    if self.current_char == "=":
                        self.advance()
                        return Token(COMPARE_GREATEREQUAL, self.line, self.column)
                    else:
                        return Token(COMPARE_GREATER, self.line, self.column)

                if self.current_char == "<":
                    self.advance()
                    if self.current_char == "=":
                        self.advance()
                        return Token(COMPARE_LESSEQUAL, self.line, self.column)
                    else:
                        return Token(COMPARE_LESS, self.line, self.column)

                if self.current_char == "!":
                    self.advance()
                    if self.current_char == "=":
                        self.advance()
                        return Token(COMPARE_NOTEQUALS, self.line, self.column)
                    else:
                        raise Exception(f"Invalid character: !")

                if self.current_char == "?":
                    self.advance()
                    if self.current_char == "=":
                        self.advance()
                        return Token(COMPARE_EQUALS, self.line, self.column)

                if self.current_char == "@" and self.peek() == "{":
                    self.advance()
                    self.advance()
                    return Token(LIST_START, self.line, self.column)

                if self.current_char == "}" and self.peek() == "@":
                    self.advance()
                    self.advance()
                    return Token(LIST_END, self.line, self.column)

                if self.current_char == "}":
                    if self.peek() != "@":
                        self.advance()
                        return Token(RBRACE, self.line, self.column)

                if self.current_char == "{":
                    if self.position == 0 or self.text[self.position-1] != "@":
                        self.advance()
                        return Token(LBRACE, self.line, self.column)

                if self.current_char == ":" and self.peek() == ":":
                    self.advance()
                    self.advance()
                    return Token(INDEX_ACCESS, self.line, self.column)

                if self.current_char == ";" :
                    self.advance()
                    return Token(SEMICOLON, self.line, self.column)

                raise PluckError(f"Invalid character: {self.current_char}", self.line, self.column)
            return Token(EOF, self.line, self.column)
        except PluckError as e:
            print(e)
            return Token(EOF, self.line, self.column)
        except Exception as e:
            print(f"Lexer error: {e}")
            return Token(EOF, self.line, self.column)