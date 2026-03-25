# 🐍 Python Day 03 – Functions & System Monitoring

## 📌 Overview

This module focuses on **functions in Python** and introduces **real-world DevOps use cases** like system monitoring using external libraries.

You learned:

* Function creation and usage
* Taking input inside functions
* Conditional execution
* Using external libraries (`psutil`)
* Monitoring system resources (RAM & CPU)

---

## 🚀 Topics Covered

---

### 🔹 1. Function Definition

```python
def add(a, b):
    return a + b
```

👉 A function that takes two inputs and returns their sum.

---

### 🔹 2. Function Calling

```python
print(add(50, 60))

x = 20
y = 40
print(add(x, y))
```

👉 Functions can be called with direct values or variables.

---

### 🔹 3. Function with User Input

```python
def sum():
    a = int(input("Enter your First Number: "))
    b = int(input("Enter your Second Number: "))
    sum = a + b
    print(f"Sum of {a} and {b} is:", sum)
```

👉 This function takes input from the user and prints the result.

---

### 🔹 4. Conditional Function Execution

```python
env = input("Enter the Environment: ")

if env == "prod":
    print("Sum is allowed in production environment")
    sum()
elif env == "stagging" or env == "dev":
    print("Sum is not allowed in staging and development environment")
else:
    print("Invalid Environment")
```

👉 Demonstrates environment-based logic (important in DevOps).

---

### 🔹 5. System Monitoring using psutil

Using **psutil** to fetch system metrics.

---

#### RAM Usage

```python
import psutil

RAM_usage = psutil.virtual_memory().percent
print(f"Current RAM usage: {RAM_usage}%")
```

---

#### RAM Threshold Check

```python
def ram_usage_threshold():
    threshold = int(input("Enter RAM threshold: "))
    if RAM_usage > threshold:
        print("Warning: RAM usage exceeded!")
    else:
        print("RAM usage is within limits")
```

---

#### CPU Usage

```python
cpu_usage = psutil.cpu_percent(interval=1)
print(f"Current CPU usage: {cpu_usage}%")
```

---

#### CPU Threshold Check

```python
def cpu_usage_threshold():
    threshold = int(input("Enter CPU threshold: "))
    if cpu_usage > threshold:
        print("Warning: CPU usage exceeded!")
    else:
        print("CPU usage is within limits")
```

---

## 🧠 Key Learnings

* Functions help in writing reusable and modular code
* Input can be taken inside or outside functions
* Conditional logic controls execution flow
* External libraries extend Python capabilities
* `psutil` helps monitor system performance
* Threshold-based checks are useful in real DevOps monitoring

---

## 📁 File Structure

```
Day_03/
 └── functions_and_monitoring.py
```

---

## 🔥 DevOps Relevance

* Automating health checks
* Monitoring system resources
* Creating alerting logic (CPU/RAM threshold)
* Environment-based execution (prod vs dev)

---

## ⚡ Improvements (Best Practices)

* Avoid overriding built-in names like `sum()`
* Use functions for logic, not input handling
* Use logging instead of print (in real projects)
* Integrate alerts (Email/Slack) instead of print

---

## 🚀 Next Steps

* Error handling (`try-except`)
* File handling
* Logging
* API integration
* Automation scripts

---

## 👨‍💻 Author

**Amit Kumar (AKKC)**
🚀 DevOps Learner | Python Enthusiast

---
