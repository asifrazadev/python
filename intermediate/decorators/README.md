# Decorators

Part of the **Intermediate Python** series. → [Back to intermediate](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **Decorator** | A function that takes another function as input, wraps its execution with additional behavior, and returns the modified function. |
| **`*args` and `**kwargs`** | Used in wrapper definitions to support functions with any signature (positional or keyword arguments). |
| **`@` Syntax** | Synthetic sugar to automatically wrap a function (e.g. `@time_it`). |

---

## 🧠 Key Concepts & Gotchas

### What are Decorators?
Decorators allow you to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it.

Common use-cases:
- **Logging**: Log when functions start and end.
- **Timing**: Measure execution time of operations.
- **Authorization**: Check if a user has access before executing.

```python
def my_decorator(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
```

### Passing Arguments
To decorate functions that accept arguments, use `*args` and `**kwargs` inside the wrapper definition.
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # Do something
        return func(*args, **kwargs)
    return wrapper
```

---

## 🚀 Run It

```powershell
python decorators.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [intermediate](../README.md)*
