class NumberNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


class StringNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'"{self.value}"'
    
class BooleanNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)
    
class FloatNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)

class BinOpNode:
    def __init__(self, left, op, right):

        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"({self.left} {self.op.type} {self.right})"


class VarAccessNode:
    def __init__(self, var_name):
        self.var_name = var_name

    def __repr__(self):
        return self.var_name


class VarAssignNode:
    def __init__(self, var_name, value_node):

        self.var_name = var_name
        self.value_node = value_node

    def __repr__(self):
        return f"({self.var_name} = {self.value_node})"


class FunctionCallNode:
    def __init__(self, name, arguments):

        self.name = name
        self.arguments = arguments

    def __repr__(self):
        return f"{self.name}({self.arguments})"


class StatementsNode:
    def __init__(self, statements):
        self.statements = statements

    def __repr__(self):
        return str(self.statements)


class CompareNode:

    def __init__(self, left, op, right):

        self.left = left
        self.op = op
        self.right = right

    def __repr__(self):
        return f"({self.left} {self.op.type} {self.right})"


class IfNode:

    def __init__(self, condition, body, elif_branches=None, else_body=None):

        self.condition = condition
        self.body = body
        self.elif_branches = elif_branches or []
        self.else_body = else_body

    def __repr__(self):
        parts = [f"IF {self.condition} THEN {self.body}"]
        for cond, bod in self.elif_branches:
            parts.append(f"ELIF {cond} THEN {bod}")
        if self.else_body:
            parts.append(f"ELSE {self.else_body}")
        return ' '.join(parts)
    
class WhileNode:

    def __init__(self, condition, body):

        self.condition = condition
        self.body = body

    def __repr__(self):
        return f"WHILE {self.condition} REPEATE {self.body}"
    
class ForNode:
    def __init__(self, var_name, start_value, end_value, body):
        self.var_name = var_name
        self.start_value = start_value
        self.end_value = end_value
        self.body = body

    def __repr__(self):
        return f"FOR {self.var_name} = {self.start_value} TO {self.end_value} DO {self.body}"
    
class FunctionDefinitionNode:
    def __init__(self, name, parameters, body):
        self.name = name
        self.parameters = parameters
        self.body = body

    def __repr__(self):
        return f"FN {self.name}({self.parameters}) {self.body}"
    
class ListNode:
    def __init__(self, elements):
        self.elements = elements
    def __repr__(self):
        return f"@{{{', '.join(map(str, self.elements))}}}"
    
class IndexAccessNode:
    def __init__(self, list_node, index_node):
        self.list_node = list_node
        self.index_node = index_node
    def __repr__(self):
        return f"{self.list_node}::({self.index_node})"
    
class ReturnNode:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"RETURN {self.value}"
    
class BreakNode:
    def __repr__(self):
        return "BREAK"