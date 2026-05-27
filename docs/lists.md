# Lists

Pluck uses a unique syntax for lists to distinguish them from code blocks and other data structures. Lists are defined using `@{ ... }@`.

## Creating a List

```
myList = @{1, 2, 3, 4, 5}@
```

## Accessing List Elements

Use the double colon `::` syntax to access elements by index:

```
out(myList::(0))  # Outputs: 1
```

## Modifying List Elements

You can assign a new value to a specific index:

```
myList::(2) = 10
out(myList)  # Outputs: [1, 2, 10, 4, 5]
```

## Appending to a List

Append a value to a list using the double colon and append method:

```
myList = @{1, 2, 3, 4, 5}@
myList::append(6)
out(myList)  # Outputs: [1, 2, 3, 4, 5, 6]
```

## List Functions

- `length(list)` — Returns the number of elements in the list.

Example:

```
out(length(myList))  # Outputs: 5
```

## Summary

- Lists use `@{ ... }@` for definition.
- Access with `::(index)`.
- Modify with assignment to `::(index)`.
- Append values with `::append(value)`.
- Use built-in functions like `length` for list operations.
- Outputed lists can be easily identified as there are wraped in square brackets `[ ... ]` unlike definition brackets `@{ ... }@`
