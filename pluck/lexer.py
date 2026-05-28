from pluck.tokens import *

class Lexer:

    def __init__(self, text):

        self.text = text
        self.position = 0

        if len(text) > 0:
            self.current_char = text[self.position]
        else:
            self.current_char = None

    def advance(self):

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
            return Token(FLOAT, float(result))
        else:
            return Token(NUMBER, int(result))

    def string(self):

        self.advance()

        result = ""

        while self.current_char is not None and self.current_char != '"':

            result += self.current_char
            self.advance()

        self.advance()

        return Token(STRING, result)
    
    def boolean(self):

        result = ""

        while self.current_char is not None and self.current_char.isalpha():

            result += self.current_char
            self.advance()

        if result == "true":
            return Token(TRUE, True)
        elif result == "false":
            return Token(FALSE, False)
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
        }

        if result in KEYWORDS:
            return Token(KEYWORDS[result])

        return Token(IDENTIFIER, result)

    def get_next_token(self):

        while self.current_char is not None:

            if self.current_char == "\n":
                self.advance()
                return Token(NEWLINE)

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
                return Token(PLUS)

            if self.current_char == "-":
                self.advance()
                return Token(MINUS)

            if self.current_char == "*":
                self.advance()
                if self.current_char == "*":
                    self.advance()
                    return Token(EXPONENT)
                return Token(MULTIPLY)

            if self.current_char == "/":
                self.advance()
                if self.current_char == "/":
                    while self.current_char is not None and self.current_char != "\n":
                        self.advance()
                    continue
                else:
                    return Token(DIVIDE)

            if self.current_char == "%":
                self.advance()
                return Token(MODULO)

            if self.current_char == "(":
                self.advance()
                return Token(LPAREN)

            if self.current_char == ")":
                self.advance()
                return Token(RPAREN)

            if self.current_char == "=":
                self.advance()
                return Token(EQUALS)

            if self.current_char == ",":
                self.advance()
                return Token(COMMA)

            if self.current_char == ">":
                self.advance()
                if self.current_char == "=":
                    self.advance()
                    return Token(COMPARE_GREATEREQUAL)
                else:
                    return Token(COMPARE_GREATER)

            if self.current_char == "<":
                self.advance()
                if self.current_char == "=":
                    self.advance()
                    return Token(COMPARE_LESSEQUAL)
                else:
                    return Token(COMPARE_LESS)

            if self.current_char == "!":
                self.advance()
                if self.current_char == "=":
                    self.advance()
                    return Token(COMPARE_NOTEQUALS)
                else:
                    raise Exception(f"Invalid character: !")

            if self.current_char == "?":
                self.advance()
                if self.current_char == "=":
                    self.advance()
                    return Token(COMPARE_EQUALS)

            if self.current_char == "@" and self.peek() == "{":
                self.advance()
                self.advance()
                return Token(LIST_START)
            
            if self.current_char == "}" and self.peek() == "@":
                self.advance()
                self.advance()
                return Token(LIST_END)
            
            if self.current_char == "}":
                if self.peek() != "@":
                    self.advance()
                    return Token(RBRACE)
                
            if self.current_char == "{":
                if self.position == 0 or self.text[self.position-1] != "@":
                    self.advance()
                    return Token(LBRACE)

            if self.current_char == ":" and self.peek() == ":":
                self.advance()
                self.advance()
                return Token(INDEX_ACCESS)
            
            if self.current_char == ";" :
                self.advance()
                return Token(SEMICOLON)

            raise Exception(f"Invalid character: {self.current_char}")

        return Token(EOF)