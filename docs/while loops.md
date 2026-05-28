# While Loops

While loops in Pluck allow you to repeat a block of code as long as a condition is true.

## Syntax

```pluck
while condition {
    // Code to repeat while condition is true
}
```

## Example

```pluck
x = 1
while x <= 5 {
    print(x)
    x = x + 1
}
```

This will print the numbers 1 through 5, each on a new line.

## Break

breaking alows you to break out of a loop and not continue completely ignorring the condition.

```pluck
while true{
    out("a")
    break
    out("b")
}
// output: a
```

## Infinite Loops

Be careful: if the condition never becomes false, the loop will run forever and may cause your program to stop responding.
