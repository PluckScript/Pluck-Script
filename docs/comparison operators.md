# Comparison Operators

Pluck supports standard comparison operators for comparing values. These are commonly used in conditions for if statements and loops.

## Operators

| Operator | Description         | Example      |
|----------|---------------------|--------------|
| >        | Greater than        | `x > y`      |
| <        | Less than           | `x < y`      |
| >=       | Greater or equal    | `x >= y`     |
| <=       | Less or equal       | `x <= y`     |
| ?=       | Equal to            | `x ?= y`     |
| !=       | Not equal to        | `x != y`     |

## Examples

```pluck
x = 5
y = 10
result1 = x < y   // true
result2 = x ?= y  // false
result3 = y >= 10 // true
```

Comparison operators are typically used in control flow statements:

```pluck
if x > 0 {
    print("x is positive")
}
```
