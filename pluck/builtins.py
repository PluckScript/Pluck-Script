class builtins:
    def builtin_out(self, *args):
        print(*args)

    def builtin_input(self, prompt=""):
        return input(prompt)

    def builtin_length(self, value):
        return len(value)

    def builtin_int(self, value):
        return int(value)

    def builtin_str(self, value):
        return str(value)

    def builtin_float(self, value):
        return float(value)