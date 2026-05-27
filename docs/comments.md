# Comments

Comments are pieces of text ignored by the Pluck interpreter. They are useful for explaining code or leaving reminders for yourself or others.

## How to Write a Comment

```pluck
// This is a comment
```

To write a comment, start the line with `//`. Anything after `//` on the same line will be ignored by the interpreter. Anything before `//` will be executed as code.

```pluck
print("hello world!") // This will display: hello world!
// Output: hello world!

// print("hello world!")
// Output: (nothing happens)
```