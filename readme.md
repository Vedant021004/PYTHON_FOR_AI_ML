# Python - Closures & Decorators Guide 

> Author: [Vedant021004](https://github.com/Vedant021004)

Closures and Decorators are advanced topics, but you don’t need super deep theory at first 👍

You only need:

* what they are
* why they are used
* basic syntax
* where companies/frameworks use them

That’s enough for now 

# Closures

## What is a Closure?

A closure is:

> a function that remembers values from another function.

---

## Example

```python
def power_factory(ex):

    def power(base):
        return base ** ex

    return power

square = power_factory(2)

print(square(5))
```

Output:

```python
25
```

---

## What happens?

```python
square = power_factory(2)
```

stores:

```python
ex = 2
```

Then:

```python
square(5)
```

does:

```python
5 ** 2
```

---

# Why Use Closures?

Because they help create:

* reusable functions
* customized functions
* memory/state

---

# Real-world Uses of Closures

## 1. Function Factories

```python
square = power_factory(2)
cube = power_factory(3)
```

---

## 2. Counters

```python
count += 1
```

---

## 3. Password Systems

Remember secret passwords internally.

---

## 4. API Configurations

Remember API keys/settings.

---

# Decorators

## What is a Decorator?

A decorator:

> adds extra behavior to a function without changing original code.

---

# Example

```python
def logger(func):

    def wrapper():
        print("Started")

        func()

        print("Ended")

    return wrapper

@logger
def hello():
    print("Hello")

hello()
```

Output:

```python
Started
Hello
Ended
```

---

# What decorator does?

It wraps another function.

Like:

```python
gift wrapper around a box
```

Original function stays same,
but extra features added.

---

# Why Use Decorators?

Because they help add:

* logging
* authentication
* timing
* security
* validation

without changing actual code.

---

# Real-world Uses of Decorators

## Flask

```python
@app.route("/")
```

---

## FastAPI

```python
@app.get("/")
```

---

## Authentication

```python
@login_required
```

---

## Timing Functions

```python
@timer
```

---

# Difference

| Closures        | Decorators           |
| --------------- | -------------------- |
| Remember values | Modify functions     |
| Store memory    | Add behavior         |
| Can work alone  | Built using closures |

---

# Easy Memory Trick

## Closure

👉 “Function with memory”

## Decorator

👉 “Function enhancer”


