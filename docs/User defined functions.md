# User-Defined Functions

User-defined functions in Pluck allow you to create reusable blocks of code that can accept parameters and be called with arguments.

## Creating a Function

Define a function using `fn`, followed by the function name and parameters in parentheses, separated by commas:

```pluck
fn greet(name, age) {
    print("Hello", name, "you are", age, "years old")
}
```

## Calling a Function

Call a function by writing its name followed by parentheses containing any arguments. The argument names do not need to match the parameter names.

```pluck
myName = "Jonah"
myAge = 14
greet(myName, myAge)
```

## Reterning a value

Returning a value allows you to input data into a function, process it, and then return a value without needing to output anything.

```pluck
fn add(a, b){
    x = a + b
    return(x)
}

z = add(1, 2)
// z = 3 but nothing was outputed
```