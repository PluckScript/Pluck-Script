# Basic Arithmetic Operations

Pluck supports standard arithmetic operations for working with numbers, including addition, subtraction, multiplication, and division.

## Operators

| Operator | Description     | Example      |
|----------|----------------|--------------|
| +        | Addition       | `x + y`      |
| -        | Subtraction    | `x - y`      |
| *        | Multiplication | `x * y`      |
| /        | Division       | `x / y`      |

## Examples

```pluck
// Addition
result = 5 + 3   // result is 8

// Subtraction
result = 10 - 4  // result is 6

// Multiplication
result = 5 * 7   // result is 35

// Division
result = 20 / 4  // result is 5
```

You can use variables and numbers together in arithmetic expressions:

```pluck
a = 2
b = 3
sum = a + b      // sum is 5
product = a * b  // product is 6
```

## Order of Operations

Pluck follows the standard order of operations (BODMAS):
- Parentheses
- Multiplication and Division
- Addition and Subtraction

```pluck
result = 2 + 3 * 4   // result is 14
result = (2 + 3) * 4 // result is 20
```