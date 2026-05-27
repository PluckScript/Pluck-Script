# Variables

Variables in Pluck allow you to store and reuse values throughout your code. They can hold numbers, strings, or booleans, and can be updated at any time.

## Creating Variables

Assign a value to a variable using the `=` operator:

```pluck
x = 10
name = "Jonah"
```

## Variable Naming Rules

- Must begin with a letter or underscore (`_`)
- Can contain letters, numbers, and underscores
- Cannot start with a number

| Valid Names    | Invalid Names |
|---------------|--------------|
| x             | 1stValue     |
| player_score  | -score       |
| _temp         | $amount      |
| name1         | 123abc       |

## Examples

```pluck
score = 100
player_health = 75
person1 = "Bob"
_temp = 42
```

## Reassigning Variables

You can update a variable's value at any time:

```pluck
x = 10
x = x + 5  // x is now 15
```

## Using Variables in Expressions

Variables can be used in arithmetic and other expressions:

```pluck
a = 2
b = 3
sum = a + b      // sum is 5
product = a * b  // product is 6
```