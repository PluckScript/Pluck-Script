# If Statements

If statements in Pluck allow you to execute code only when a condition is true. You can also use `elif` and `else` to check multiple conditions or provide a fallback.

## Syntax

```pluck
if condition {
    // Code to execute if condition is true
}
elif other_condition {
    // Code to execute if other_condition is true
}
else {
    // Code to execute if no previous condition is true
}
```

## Example

```pluck
x = 10
if x > 10 {
    print("x is greater than 10")
}
elif x ?= 10 {
    print("x is exactly 10")
}
else {
    print("x is less than 10")
}
```

You can use any comparison or arithmetic expression as the condition.

## Nested If Statements

If statements can be nested inside each other:

```pluck
x = 7
if x > 0 {
    if x < 10 {
        print("x is between 1 and 9")
    }
}
```
