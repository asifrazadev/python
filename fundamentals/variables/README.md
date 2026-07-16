# Variables & Data Types

Part of the **Python Fundamentals** series. → [Back to fundamentals](../README.md)

---

## 📖 What's Covered

| Section | Key Points |
|---------|-----------|
| Basic assignment | `name = "Alice"`, `age = 30`, `is_student = True`, `nothing = None` |
| Multiple assignment | `x = y = z = 0`, `a, b, c = 1, 2, 3` |
| Starred unpacking | `first, *rest = [10, 20, 30, 40]` |
| Swap without temp | `a, b = b, a` |
| Type hints (PEP 526) | `username: str = "bob"` — annotations only, NOT enforced |
| Constants | `UPPER_CASE` by convention, e.g. `MAX_RETRIES: int = 5` |
| `id()` | Returns memory address — `m is n` checks identity (same object) |
| `del` | Removes a name binding from scope |

---

## 🧠 Key Concepts & Gotchas

### Python is dynamically typed
```python
x = 42        # int
x = "hello"   # now str — Python allows this
```

### `None` is not `0` or `False`
```python
nothing = None
bool(nothing)  # False — but it's its own type: NoneType
```

### Starred unpacking
```python
first, *rest = [10, 20, 30, 40]
# first = 10, rest = [20, 30, 40]

*init, last = [10, 20, 30, 40]
# init = [10, 20, 30], last = 40
```

### Type hints are NOT enforcement
```python
score: int = "oops"   # No error at runtime — hints are for tools (mypy, IDEs)
```

### Constants: convention only
Python has no `const` keyword. `UPPER_CASE` is just a signal to other developers.

### `is` vs `==`
```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b   # True  — same value
a is b   # False — different objects in memory
```
Small integers (-5 to 256) are cached, so `42 is 42` happens to be `True` — don't rely on this.

### `del` unbinds the name, doesn't destroy the object
```python
temp = "hello"
del temp         # name 'temp' is gone from scope
                 # the string object itself is GC'd when no references remain
```

---

## 🚀 Run It

```powershell
python variables.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [fundamentals](../README.md)*
