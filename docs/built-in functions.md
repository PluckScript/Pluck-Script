# Built-in Functions

Pluck provides several built-in functions to help you interact with your program and perform common tasks.

## out

Outputs values to the console.

```pluck
out("Hello, world!")
x = 5
out(x)
```

## input

Reads a line of input from the user. Optionally, you can provide a prompt.

```pluck
name = input("What is your name? ")
out("Hello,", name)
```

## length

Returns the length of a string.

```pluck
text = "hello"
length = length(text)  // length is 5
```

## int, str, float

Converts values between types.

```pluck
x = "123"
y = int(x)    // y is 123 (number)
z = str(y)    // z is "123" (string)
```

