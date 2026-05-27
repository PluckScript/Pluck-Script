# PLUCK

PLUCK is a lightweight interpreted scripting language written in Python.

It is designed to be simple, expressive, and beginner-friendly while still supporting core programming language features such as functions, loops, conditionals, collections, and modular syntax.

---

# Features

## Core Language Features

- Variables
- Arithmetic expressions
- Boolean logic
- Conditionals (`if`, `elif`, `else`)
- Loops (`while`, `for`)
- User-defined functions
- Built-in functions
- Lists / arrays
- List indexing and mutation
- Comments

---

# Example

```pluck
numbers = @{1,2,3}@

numbers::append(4)

out(numbers)
```

Output:

```txt
[1, 2, 3, 4]
```

---

# Syntax Overview

## Variables

```pluck
x = 10
name = "Jonah"
```

## Conditionals

```pluck
if x > 5 {
    out("big")
}
```

## Functions

```pluck
fn greet(name) {
    out("Hello", name)
}

greet("PLUCK")
```

## Lists

```pluck
items = @{1,2,3}@

out(items::(0))
```

---

# Project Goals

PLUCK aims to evolve into a fully usable interpreted scripting language with:

- modules/imports
- improved tooling
- better error handling
- REPL support
- syntax highlighting
- package management
- standard library support

---

# Project Structure

```txt
PLUCK/
│
├── pluck/
├── examples/
├── docs/
├── tests/
└── main.py
```

---

# Running PLUCK

```bash
python main.py examples/test.plk
```

---

# Current Status

PLUCK is currently in active development.

Version:
```txt
v0.1.0
```

---

# Roadmap

- return statements
- modules/imports
- dictionaries/maps
- improved runtime scope system
- REPL
- syntax highlighting
- package manager

---

# License

MIT License
