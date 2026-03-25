
# 🐍 Python Day 02 – Loops & Control Flow

## 📌 Overview

This module focuses on **loops and control flow in Python**, which are essential for automation and DevOps scripting.
You learned how to iterate over data, control execution flow, and interact with user input.

---

## 🚀 Topics Covered

---

### 🔹 1. For Loop

Used to iterate over sequences like lists or ranges.

```python
a = int(input("Enter a number: "))
for i in range(a):
    print(i)
```

👉 Prints numbers from `0` to `a-1`

---

### 🔹 2. Loop with List

```python
numbers = [1,2,3,4,5,6,7,8,9,10]
for i in numbers:
    if i == 6:
        break
    print(i)

print("List has been printed")
```

👉 Stops loop when value becomes `6` using `break`

---

### 🔹 3. Nested Loops

```python
for i in range(5):
    for j in range(3):
        print(i, j)
```

👉 Loop inside another loop (used in matrices, patterns, etc.)

---

### 🔹 4. Loop Control with User Input

```python
for i in range(10):
    print("This is iteration number ", i)
    itr = input("Do you want to continue? (y/n): ")
    if itr.lower() == 'n':
        print("Exiting the loop")
        break
```

👉 Allows dynamic control over loop execution

---

### 🔹 5. Multiplication Table Generator

```python
number = int(input("Enter a number to get Table: "))
for i in range(1,11):
    print(number, "x", i, "=", number*i)
```

👉 Prints table from 1 to 10

---

### 🔹 6. While Loop (Interactive Program)

```python
choice = input("Enter Your Choice (press q to quit): ")

while choice != 'q':
    number = int(input("Enter a number to get Table: "))
    print(f"Table of - {number} is Below:-")

    for i in range(1,11):
        print(number, "x", i, "=", number*i)

    choice = input("Enter Your Choice (press q to quit): ")
```

👉 Keeps running until user enters `q`

---

### 🔹 7. Conditional Logic (Environment-based)

```python
env = input("Enter the environment you want to work in (dev, staging, prod): ")

if env == "prod":
    print("App Deployment is not allowed in production environment")
elif env == "staging" or env == "dev":
    print("App Deployment is allowed only in staging and development environment")
else:
    print("Invalid environment")
```

---

### 🔹 8. Advanced Conditional Logic

```python
if env == "prod":
    print("Deployment is not allowed on Friday in production environment")

elif env == "staging":
    print("Take backup and test before deploying to production")

elif env == "dev":
    print("Deployment is allowed on all days")

else:
    print("Invalid environment")
```

---

## 🧠 Key Learnings

* `for` loop is used for iteration over sequences
* `while` loop runs until a condition becomes false
* `break` exits the loop immediately
* Nested loops allow multi-level iteration
* User input can dynamically control program flow
* Conditional statements (`if-elif-else`) are critical for decision-making
* Logical operators (`and`, `or`) help in complex conditions

---

## 📁 File Structure

```
Day_02/
 └── loops_and_conditions.py
```

---

## 🎯 DevOps Relevance

* Looping over servers/resources
* Automating repetitive tasks
* Environment-based deployment logic
* Interactive scripts for automation

---

## 🚀 Next Steps

* Functions (modular coding)
* Lists & Dictionaries (data handling)
* Exception handling
* File handling

---

## 👨‍💻 Author

**Amit Kumar (AKKC)**
🚀 DevOps Learner | Python Enthusiast

---

