# Errors and Exceptions

Pluck provides error messages for common mistakes such as:
- Syntax errors
- Undefined variables
- Invalid operations (e.g., dividing by zero)
- Type errors (e.g., adding a string to a number)

## Example

```pluck
out(x) // Error: Undefined variable: x
```

### Control Flow Exceptions
- `return` — Exits a function and returns a value.
- `break` — Exits a loop immediately.

These are handled internally and do not print errors unless misused.

## Error Message Format
Errors include a message and, when possible, line and column information:

```
Error: <message> line: <line>, column: <column>
```

## Best Practices
- Check variable names for typos.
- Use correct types in expressions.
- Use `break` only inside loops.
- Use `return` only inside functions.
