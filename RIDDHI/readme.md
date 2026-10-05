# 🐍 Python OOP + Basics Practice Set

## 🟢 LEVEL 1 — Easy

### Conditions

* [X] **1.** Write a program to check whether a number is positive, negative, or zero.

* [X] **2.** Write a program to check whether a number is even or odd.

* [X] **3.** Take age as input and print whether the person is eligible to vote.

* [X] **4.** Take three numbers and print the largest number using `if-elif-else`.

* [X] **5.** Check whether a given year is a leap year.

---

### Functions

* [X] **6.** Create a function `greet()` that prints `"Hello Python"`.

* [X] **7.** Create a function that accepts a name and prints `"Hello Vedant"`.

* [X] **8.** Create a function that accepts two numbers and returns their sum.

* [X] **9.** Create a function that accepts a number and returns whether it is even or odd.

* [X] **10.** Create a function that accepts three numbers and returns the largest.

---

### `try/except`

* [X] **11.** Ask the user for two numbers and divide them. Handle division by zero.

* [X] **12.** Ask the user to enter an integer. Handle the case where the user enters text.

* [X] **13.** Write a program that handles both `ValueError` and `ZeroDivisionError`.

* [ ] **14.** Create a program using `try`, `except`, and `finally`.

* [ ] **15.** Write a program that tries to access an index that doesn't exist and handles the error.

---

# 🟡 LEVEL 2 — Classes & Objects

### Class and Object

* [X] **16.** Create a `Car` class with a method `drive()` that prints `"Car is driving"`.

* [X] **17.** Create a `Student` class with `name` and `age` attributes.

* [X] **18.** Create a `Car` class with `brand` and `model` using `__init__()`.
Example:

```text
car = Car("Toyota", "Fortuner")
```

* [X] **19.** Create a `Person` class with `name` and `age`, then create **three objects**.

* [X] **20.** Create a `BankAccount` class with `name` and `balance`, then create an object and print both.

---

# 🟡 LEVEL 3 — Functions + OOP

* [X] **21.** Create a `Calculator` class with methods:

  * `add()`
  * `subtract()`
  * `multiply()`
  * `divide()`

* [X] **22.** Create a `Car` class with:

  * `brand`
  * `model`
  * `year`
  * `display_info()`

* [ ] **23.** Create a `Student` class with:

  * `name`
  * `marks`
  * `result()`

`result()` should print `"Pass"` if marks ≥ 40, otherwise `"Fail"`.

* [ ] **24.** Create a `BankAccount` class with:

  * `deposit()`
  * `withdraw()`
  * `show_balance()`

Use conditions to prevent withdrawal if the balance is insufficient.

* [ ] **25.** Add `try/except` to your BankAccount program to handle invalid input.

---

# 🟠 LEVEL 4 — Inheritance

* [ ] **26.** Create an `Animal` class with an `eat()` method. Create a `Dog` class that inherits from `Animal`.

Expected:

```text
dog.eat()
```

should work.

* [ ] **27.** Create:

```text
Animal
   ↓
Dog
```

Animal should have:

```text
eat()
sleep()
```

Dog should have:

```text
bark()
```

Make all three methods work from a Dog object.

* [ ] **28.** Create a `Car` class with `brand` and `model`. Create an `ElectricCar` class that inherits from `Car` and adds `battery`.

* [ ] **29.** Create:

```text
Person
   ↓
Student
```

Person should have `name` and `age`.

Student should additionally have `course`.

* [ ] **30.** Create:

```text
Animal
   ↓
Dog
   ↓
Puppy
```

Give each class one unique method and call all three methods using a Puppy object.

---

# 🔴 LEVEL 5 — `super()`

* [ ] **31.** Create a `Car` class with:

```python
__init__(self, brand)
```

Create an `ElectricCar` class with:

```python
__init__(self, brand, battery)
```

Use:

```python
super().__init__()
```

to initialize `brand`.

* [ ] **32.** Create:

```text
Person
   ↓
Student
```

Person:

```text
name
age
```

Student:

```text
course
```

Use `super()`.

* [ ] **33.** Create a `Car` class with a `start()` method.

Override `start()` in `ElectricCar` and use:

```python
super().start()
```

Then print an additional message.

Expected idea:

```text
Car is starting
Electric motor is starting
```

* [ ] **34.** Create:

```text
Animal
   ↓
Dog
```

Animal:

```python
speak()
```

Dog overrides `speak()` but also calls the parent's `speak()` using `super()`.

* [ ] **35.** Create a `Vehicle` class with `__init__(brand, model)` and a `Car` class with an additional `color`.

Use `super()` to initialize the parent properties.

---

# 🔴 LEVEL 6 — Method Overriding

* [ ] **36.** Create a `Car` class with:

```python
def start(self):
    print("Car starts")
```

Override `start()` inside `ElectricCar`.

* [ ] **37.** Create:

```text
Animal
   ↓
Dog
```

Animal:

```python
speak()
```

Dog should override `speak()` and print `"Dog barks"`.

* [ ] **38.** Create:

```text
Vehicle
   ↓
Car
   ↓
ElectricCar
```

Give each class a `start()` method.

Observe which method executes when you create an `ElectricCar`.

* [ ] **39.** Override a parent's `drive()` method and use `super().drive()` so that **both parent and child messages appear**.

* [ ] **40.** Create a `Fruit` class with `kiwi()` and a `Veg` class that overrides `kiwi()`. Use `super()` to execute both versions.

---

# 🔴 LEVEL 7 — Method Overloading in Python

Remember: Python doesn't have traditional Java-style method overloading. Practice using **default arguments**.

* [ ] **41.** Create a `Calculator` class with an `add()` method that can handle:

```text
add()
add(10)
add(10, 20)
```

* [ ] **42.** Create a `Car` class with a `start()` method that can handle:

```text
start()
start("Key")
start("Key", "Sport")
```

Use default parameters.

* [ ] **43.** Create a `Student` class with a `display()` method that can display:

```text
name
name + age
name + age + course
```

using default parameters.

* [ ] **44.** Create a `Calculator` using `*args` so that:

```text
add(5, 10)
add(5, 10, 20)
add(5, 10, 20, 30)
```

all work.

* [ ] **45.** Explain in your own words the difference between **overriding** and **overloading**.

---

# 🔥 LEVEL 8 — Mixed Challenges

These are where you should **stop copying examples** and start thinking.

* [ ] **46.** Build a `Car` → `ElectricCar` program that contains:

  * `__init__()`
  * inheritance
  * `super().__init__()`
  * method overriding
  * `super().method()`

* [ ] **47.** Build an `Animal` → `Dog` program where:

  * Animal has `name`
  * Animal has `eat()`
  * Dog has `breed`
  * Dog overrides `eat()`
  * Dog uses `super().eat()`

* [ ] **48.** Build a `BankAccount` class with:

  * `__init__()`
  * deposit
  * withdrawal
  * conditions
  * `try/except`

* [ ] **49.** Build:

```text
Vehicle
   ↓
Car
   ↓
ElectricCar
```

Requirements:

* Vehicle → `brand`

* Car → `model`

* ElectricCar → `battery`

* Use `super()`

* Override `start()`

* Use `super().start()`

* [ ] **50.** 🔥 **Final Challenge**

Build a complete:

```text
        Vehicle
           ↓
          Car
        ↙     ↘
ElectricCar   SportsCar
```

Include:

* [ ] `__init__()`
* [ ] inheritance
* [ ] `super().__init__()`
* [ ] normal methods
* [ ] method overriding
* [ ] `super().method()`
* [ ] conditions
* [ ] functions/methods
* [ ] `try/except`
* [ ] default arguments for a method that accepts different numbers of arguments

---

# 🎯 Your Progress Tracker

```text
Conditions             [ ] 1–5
Functions              [ ] 6–10
try/except              [ ] 11–15
Classes & Objects       [ ] 16–20
Functions + OOP         [ ] 21–25
Inheritance             [ ] 26–30
super()                 [ ] 31–35
Method Overriding       [ ] 36–40
Method Overloading      [ ] 41–45
Mixed OOP               [ ] 46–50
```

### Your target

Don't just get the code to run. For every question, make sure you can answer:

> **"Why does this code work?"**

If you can complete **1–50 without looking at your previous examples**, your foundation from **conditions → functions → exceptions → inheritance → `super()` → overriding → overloading** will be very solid. 🚀
