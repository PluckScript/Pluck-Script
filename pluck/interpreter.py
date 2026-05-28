from pluck.tokens import *
from pluck.nodes import *
from pluck.errors import *
from pluck.builtins import builtins

class Interpreter(builtins):

    def __init__(self, parser):

        self.parser = parser

        self.variables = {}

        self.functions = {}

        self.builtins = {
            "out": self.builtin_out,
            "input": self.builtin_input,
            "length": self.builtin_length,
            "int": self.builtin_int,
            "str": self.builtin_str,
            "float": self.builtin_float,
        }

    def visit(self, node):

        method_name = f"visit_{type(node).__name__}"

        method = getattr(self, method_name)

        return method(node)

    
    def visit_NumberNode(self, node):
        return node.value

    def visit_StringNode(self, node):
        return node.value
    
    def visit_BooleanNode(self, node):
        return node.value
    
    def visit_FloatNode(self, node):
        return node.value

    def visit_BinOpNode(self, node):

        left = self.visit(node.left)
        right = self.visit(node.right)

        if node.op.type == PLUS:
            return left + right

        elif node.op.type == MINUS:
            return left - right

        elif node.op.type == MULTIPLY:
            return left * right

        elif node.op.type == DIVIDE:
            return left / right

        elif node.op.type == MODULO:
            return left % right

        elif node.op.type == EXPONENT:
            return left ** right

    def visit_VarAccessNode(self, node):

        if node.var_name not in self.variables:
            raise Exception(f"Undefined variable: {node.var_name}")

        return self.variables[node.var_name]

    def visit_VarAssignNode(self, node):

        if isinstance(node.var_name, IndexAccessNode):
            list_obj = self.visit(node.var_name.list_node)
            idx = self.visit(node.var_name.index_node)
            value = self.visit(node.value_node)
            list_obj[idx] = value
            return value
        else:
            value = self.visit(node.value_node)
            self.variables[node.var_name] = value
            return value

    def visit_FunctionCallNode(self, node):

        if isinstance(node.name, tuple) and node.name[0] == "list_method":
            method = node.name[1]
            if method == "append":
                list_obj = self.visit(node.arguments[0])
                value = self.visit(node.arguments[1])
                list_obj.append(value)
                return None
            else:
                raise Exception(f"Unknown list method: {method}")

        if node.name in self.builtins:

            arguments = []

            for arg in node.arguments:
                arguments.append(self.visit(arg))

            function = self.builtins[node.name]

            return function(*arguments)

        elif node.name in self.functions:

            function = self.functions[node.name]

            arguments = []

            for arg in node.arguments:
                arguments.append(self.visit(arg))

            previous_variables = self.variables.copy()

            for parameter, value in zip(
                function.parameters,
                arguments
            ):
            

                self.variables[parameter] = value

            try:
                result = self.visit(function.body)

            except returnException as return_value:

                result = return_value.value

            self.variables = previous_variables

            return result

        raise Exception(
            f"Unknown function: {node.name}"
        )

    def visit_CompareNode(self, node):

        left = self.visit(node.left)
        right = self.visit(node.right)

        if node.op.type == COMPARE_GREATER:
            return left > right

        elif node.op.type == COMPARE_LESS:
            return left < right

        elif node.op.type == COMPARE_EQUALS:
            return left == right

        elif node.op.type == COMPARE_NOTEQUALS:
            return left != right
        
        elif node.op.type == COMPARE_GREATEREQUAL:
            return left >= right
        
        elif node.op.type == COMPARE_LESSEQUAL:
            return left <= right

    def visit_IfNode(self, node):

        if self.visit(node.condition):
            return self.visit(node.body)
        for elif_cond, elif_body in node.elif_branches:
            if self.visit(elif_cond):
                return self.visit(elif_body)
        if node.else_body:
            return self.visit(node.else_body)

    def visit_WhileNode(self, node):
        while self.visit(node.condition):
            try:
                self.visit(node.body)
            except breakException:
                break
                

    def visit_ForNode(self, node):
        start = self.visit(node.start_value)
        end = self.visit(node.end_value)
        for i in range(start, end + 1):
            try:
                self.variables[node.var_name] = i
                self.visit(node.body)
            except breakException:
                break

    def visit_FunctionDefinitionNode(self, node):

        self.functions[node.name] = node

        return None
    
    def visit_ListNode(self, node):
        return [self.visit(element) for element in node.elements]
    
    def visit_IndexAccessNode(self, node):
        list_obj = self.visit(node.list_node)
        idx = self.visit(node.index_node)
        return list_obj[idx]

    def visit_StatementsNode(self, node):
        result = None
        for statement in node.statements:
            result = self.visit(statement)
        return result
    
    def visit_ReturnNode(self, node):
        value = self.visit(node.value)
        raise returnException(value)
    
    def visit_BreakNode(self, node):
        raise breakException()