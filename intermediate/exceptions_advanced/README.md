# Raise Exception and Finally

Part of the **Intermediate Python** series. → [Back to intermediate](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **`raise`** | Forces a specified exception to occur. |
| **`finally`** | A code block that is guaranteed to run, whether an exception occurred or not. |
| **Custom Exceptions** | User-defined exceptions created by inheriting from the built-in `Exception` class. |

---

## 🧠 Key Concepts & Gotchas

### Custom Exceptions
Create custom exceptions to handle domain-specific errors in your application (e.g. `InsufficientFundsError`).
```python
class InsufficientFundsError(Exception):
    pass
```

### The Power of `finally`
Commonly used to clean up external resources, like closing files, releasing locks, or closing database connections.
Even if you return from inside a `try` block, or raise an unhandled exception, the `finally` block **will execute** before exit.
```python
try:
    f = open("data.txt")
    # do something
finally:
    f.close()  # Guaranteed to run and release the file descriptor
```

### Re-raising Exceptions
Use a bare `raise` statement inside an `except` block to re-throw the currently caught exception.
```python
except ValueError:
    print("Logged locally")
    raise  # bubble up to caller
```

---

## 🚀 Run It

```powershell
python exceptions_advanced.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [intermediate](../README.md)*
