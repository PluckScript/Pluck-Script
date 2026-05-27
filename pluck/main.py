from pluck.lexer import Lexer
from pluck.parser import Parser
from pluck.interpreter import Interpreter

import sys


if len(sys.argv) < 2:

    print("Usage: python main.py <file.plk>")

    exit()


filename = sys.argv[1]


with open(filename, "r") as file:

    code = file.read()


lexer = Lexer(code)

parser = Parser(lexer)


tree = parser.statements()


print("AST:")
print(tree)

print("\nOUTPUT:")


interpreter = Interpreter(parser)

interpreter.visit(tree)