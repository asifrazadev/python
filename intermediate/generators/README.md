# Generators

Part of the **Intermediate Python** series. → [Back to intermediate](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **Generator Function** | A function defined with `def` but containing `yield` statements to produce values lazily. |
| **`yield`** | Temporarily pauses execution, returns a value, and saves the function's local state. |
| **Generator Expression** | A memory-efficient syntax representing a generator, looking like `(x for x in iterable)`. |

---

## 🧠 Key Concepts & Gotchas

### Why Use Generators?
Generators are **memory efficient**. 

If you want to read a 10GB log file:
- A normal function reads the entire file into a list (causing a memory crash).
- A generator yields lines one-by-one, keeping only one line in memory at any point.

```python
# List comprehension (allocates memory for 1M items immediately)
squares_list = [x * x for x in range(1000000)]

# Generator expression (computes values only on-demand)
squares_gen  = (x * x for x in range(1000000))
```

### Yield vs Return
- `return` terminates the function completely.
- `yield` pauses the function, returns a value to the caller, and resumes right where it left off when `next()` is called again.

---

## 🚀 Run It

```powershell
python generators.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [intermediate](../README.md)*
