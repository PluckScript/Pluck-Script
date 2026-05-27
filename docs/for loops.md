# For Loops

For loops in Pluck allow you to repeat a block of code a specific number of times using a loop variable.

## Syntax

```pluck
for i = start; end {
    // Code to repeat; i goes from start to end (inclusive)
}
```

## Example

```pluck
for i = 1; 5 {
    print(i)
}
```

This will print the numbers 1 through 5, each on a new line.

## Loop Variable

The loop variable (e.g., `i`) is assigned each value from `start` to `end` for each iteration.

## Nested For Loops

You can nest for loops inside each other:

```pluck
for x = 1; 3 {
    for y = 1; 2 {
        print(x, y)
    }
}
```
