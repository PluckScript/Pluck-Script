from pluck.tokens import *
from pluck.nodes import *

class Parser:

    def __init__(self, lexer):

        self.lexer = lexer

        self.current_token = self.lexer.get_next_token()
        self.next_token = self.lexer.get_next_token()

    def advance(self):

        self.current_token = self.next_token
        self.next_token = self.lexer.get_next_token()

    def eat(self, token_type):

        if self.current_token.type == token_type:
            self.advance()
        else:
            raise Exception(f"Expected {token_type}, got {self.current_token.type}")

    def factor(self):

        token = self.current_token

        if token.type == MINUS:
            self.eat(MINUS)
            node = self.factor()
            return BinOpNode(NumberNode(0), Token(MINUS), node)

        if token.type == NUMBER:

            self.eat(NUMBER)

            return NumberNode(token.value)

        elif token.type == STRING:

            self.eat(STRING)

            return StringNode(token.value)
        
        elif token.type == TRUE:

            self.eat(TRUE)

            return BooleanNode(True)
        
        elif token.type == FALSE:

            self.eat(FALSE)

            return BooleanNode(False)
        
        if token.type == FLOAT:

            self.eat(FLOAT)

            return FloatNode(token.value)

        if token.type == LIST_START:

            self.eat(LIST_START)

            elements = []

            if self.current_token.type != LIST_END:
                elements.append(self.assignment())
                while self.current_token.type == COMMA:
                    self.eat(COMMA)
                    elements.append(self.assignment())

            self.eat(LIST_END)

            node = ListNode(elements)

            while self.current_token.type == INDEX_ACCESS:
                self.eat(INDEX_ACCESS)
                if self.current_token.type == LPAREN:
                    self.eat(LPAREN)
                    index = self.expr()
                    self.eat(RPAREN)
                    var_name = IndexAccessNode(var_name, index)

                else:
                    raise Exception("only list indexing allowed in assignment target")

            return node

        elif token.type == IDENTIFIER:

            name = token.value

            self.eat(IDENTIFIER)

            node = VarAccessNode(name)

            while True:

                if self.current_token.type == LPAREN:

                    self.eat(LPAREN)

                    arguments = []

                    if self.current_token.type != RPAREN:

                        arguments.append(self.expr())

                        while self.current_token.type == COMMA:

                            self.eat(COMMA)

                            arguments.append(self.expr())

                    self.eat(RPAREN)

                    if isinstance(node, VarAccessNode):

                        node = FunctionCallNode(
                            node.var_name,
                            arguments
                        )

                    else:
                        raise Exception(
                            "Cannot call non-function"
                        )

                elif self.current_token.type == INDEX_ACCESS:

                    self.eat(INDEX_ACCESS)

                    if (
                        self.current_token.type == IDENTIFIER
                    ):

                        method_name = self.current_token.value

                        self.eat(IDENTIFIER)

                        self.eat(LPAREN)

                        arguments = []

                        if self.current_token.type != RPAREN:

                            arguments.append(self.expr())

                            while self.current_token.type == COMMA:

                                self.eat(COMMA)

                                arguments.append(self.expr())

                        self.eat(RPAREN)

                        node = FunctionCallNode(
                            ("list_method", method_name),
                            [node] + arguments
                        )

                    else:

                        self.eat(LPAREN)

                        index = self.expr()

                        self.eat(RPAREN)

                        node = IndexAccessNode(
                            node,
                            index
                        )

                else:
                    break

            return node

        elif token.type == LPAREN:

            self.eat(LPAREN)

            node = self.expr()

            self.eat(RPAREN)

            return node

    def term(self):

        node = self.power()

        while self.current_token.type in (MULTIPLY, DIVIDE, MODULO):

            token = self.current_token

            if token.type == MULTIPLY:
                self.eat(MULTIPLY)

            elif token.type == DIVIDE:
                self.eat(DIVIDE)

            elif token.type == MODULO:
                self.eat(MODULO)

            node = BinOpNode(node, token, self.power())

        return node

    def power(self):

        node = self.atom()

        while self.current_token.type == EXPONENT:
            token = self.current_token
            self.eat(EXPONENT)
            node = BinOpNode(node, token, self.atom())

        return node

    def atom(self):
        return self.factor()

    def expr(self):

        node = self.term()

        while self.current_token.type in (PLUS, MINUS):

            token = self.current_token

            if token.type == PLUS:
                self.eat(PLUS)

            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinOpNode(node, token, self.term())

        return node

    def assignment(self):

        if (
            self.current_token.type == IDENTIFIER
            and self.next_token.type == EQUALS
        ):

            var_name = self.current_token.value

            self.eat(IDENTIFIER)
            self.eat(EQUALS)

            value = self.expr()

            return VarAssignNode(
                var_name,
                value
            )

        left = self.expr()

        if self.current_token.type == EQUALS:

            self.eat(EQUALS)

            value = self.expr()

            return VarAssignNode(
                left,
                value
            )

        return left

    def statements(self):

        statements = []

        while self.current_token.type == NEWLINE:
            self.eat(NEWLINE)

        while self.current_token.type != EOF:

            if self.current_token.type == IF:
                statement = self.if_statement()
            elif self.current_token.type == WHILE:
                statement = self.while_statement()
            elif self.current_token.type == FOR:
                statement = self.for_statement()
            elif self.current_token.type == FN:
                statement = self.function_definition()
            else:
                statement = self.assignment()

            statements.append(statement)

            while self.current_token.type == NEWLINE:
                self.eat(NEWLINE)

        return StatementsNode(statements)

    def comparison(self):

        node = self.expr()

        while self.current_token.type in (
            COMPARE_GREATEREQUAL,
            COMPARE_GREATER,
            COMPARE_LESSEQUAL,
            COMPARE_LESS,
            COMPARE_NOTEQUALS,
            COMPARE_EQUALS,
        ):

            token = self.current_token

            if token.type == COMPARE_GREATER:
                self.eat(COMPARE_GREATER)

            elif token.type == COMPARE_LESS:
                self.eat(COMPARE_LESS)

            elif token.type == COMPARE_NOTEQUALS:
                self.eat(COMPARE_NOTEQUALS)

            elif token.type == COMPARE_EQUALS:
                self.eat(COMPARE_EQUALS)

            elif token.type == COMPARE_GREATEREQUAL:
                self.eat(COMPARE_GREATEREQUAL)

            elif token.type == COMPARE_LESSEQUAL:
                self.eat(COMPARE_LESSEQUAL)

            node = CompareNode(node, token, self.expr())

            return node

    def if_statement(self):

        self.eat(IF)

        condition = self.comparison()

        self.eat(LBRACE)

        statements = []

        while self.current_token.type == NEWLINE:
            self.eat(NEWLINE)

        while self.current_token.type != RBRACE:
            if self.current_token.type == IF:
                statement = self.if_statement()
            elif self.current_token.type == WHILE:
                statement = self.while_statement()
            elif self.current_token.type == FOR:
                statement = self.for_statement()
            else:
                statement = self.assignment()

            statements.append(statement)

            while self.current_token.type == NEWLINE:
                self.eat(NEWLINE)

        self.eat(RBRACE)

        body = StatementsNode(statements)

        elif_branches = []
        else_body = None

        while True:
            while self.current_token.type == NEWLINE:
                self.eat(NEWLINE)
            if self.current_token.type == ELIF:
                self.eat(ELIF)
                elif_cond = self.comparison()
                self.eat(LBRACE)
                elif_statements = []
                while self.current_token.type == NEWLINE:
                    self.eat(NEWLINE)
                while self.current_token.type != RBRACE:
                    if self.current_token.type == IF:
                        statement = self.if_statement()
                    elif self.current_token.type == WHILE:
                        statement = self.while_statement()
                    elif self.current_token.type == FOR:
                        statement = self.for_statement()
                    else:
                        statement = self.assignment()
                    elif_statements.append(statement)
                    while self.current_token.type == NEWLINE:
                        self.eat(NEWLINE)
                self.eat(RBRACE)
                elif_branches.append((elif_cond, StatementsNode(elif_statements)))
            elif self.current_token.type == ELSE:
                self.eat(ELSE)
                self.eat(LBRACE)
                else_statements = []
                while self.current_token.type == NEWLINE:
                    self.eat(NEWLINE)
                while self.current_token.type != RBRACE:
                    if self.current_token.type == IF:
                        statement = self.if_statement()
                    elif self.current_token.type == WHILE:
                        statement = self.while_statement()
                    elif self.current_token.type == FOR:
                        statement = self.for_statement()
                    else:
                        statement = self.assignment()
                    else_statements.append(statement)
                    while self.current_token.type == NEWLINE:
                        self.eat(NEWLINE)
                self.eat(RBRACE)
                else_body = StatementsNode(else_statements)
                break
            else:
                break
        return IfNode(condition, body, elif_branches, else_body)
    
    def while_statement(self):

        self.eat(WHILE)

        condition = self.comparison()

        self.eat(LBRACE)

        statements = []

        while self.current_token.type == NEWLINE:
            self.eat(NEWLINE)

        while self.current_token.type != RBRACE:
            if self.current_token.type == IF:
                statement = self.if_statement()
            elif self.current_token.type == WHILE:
                statement = self.while_statement()
            elif self.current_token.type == FOR:
                statement = self.for_statement()
            else:
                statement = self.assignment()

            statements.append(statement)

            while self.current_token.type == NEWLINE:
                self.eat(NEWLINE)

        self.eat(RBRACE)

        return WhileNode(condition, StatementsNode(statements))
    
    def for_statement(self):

        self.eat(FOR)

        var_name = self.current_token.value

        self.eat(IDENTIFIER)
        self.eat(EQUALS)

        start_value = self.expr()

        self.eat(SEMICOLON)

        end_value = self.expr()

        self.eat(LBRACE)

        statements = []

        while self.current_token.type == NEWLINE:
            self.eat(NEWLINE)

        while self.current_token.type != RBRACE:
            if self.current_token.type == IF:
                statement = self.if_statement()
            elif self.current_token.type == WHILE:
                statement = self.while_statement()
            elif self.current_token.type == FOR:
                statement = self.for_statement()
            else:
                statement = self.assignment()

            statements.append(statement)

            while self.current_token.type == NEWLINE:
                self.eat(NEWLINE)

        self.eat(RBRACE)

        return ForNode(var_name, start_value, end_value, StatementsNode(statements))

    def function_definition(self):

        self.eat(FN)

        function_name = self.current_token.value

        self.eat(IDENTIFIER)

        self.eat(LPAREN)

        parameters = []

        if self.current_token.type != RPAREN:
            parameters.append(self.current_token.value)
            self.eat(IDENTIFIER)

            while self.current_token.type == COMMA:
                self.eat(COMMA)
                parameters.append(self.current_token.value)
                self.eat(IDENTIFIER)

        self.eat(RPAREN)

        self.eat(LBRACE)

        while self.current_token.type == NEWLINE:
            self.eat(NEWLINE)

        statements = []

        while self.current_token.type != RBRACE:
            if self.current_token.type == IF:
                statement = self.if_statement()
            elif self.current_token.type == WHILE:
                statement = self.while_statement()
            elif self.current_token.type == FOR:
                statement = self.for_statement()
            else:
                statement = self.assignment()

            statements.append(statement)

            while self.current_token.type == NEWLINE:
                self.eat(NEWLINE)

        self.eat(RBRACE)

        return FunctionDefinitionNode(function_name, parameters, StatementsNode(statements))
