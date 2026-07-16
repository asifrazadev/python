# If Conditions

Part of the **Python Fundamentals** series. → [Back to fundamentals](../README.md)

---

## 📖 What's Covered

| Section | Key Points |
|---------|-----------|
| `if / elif / else` | Grade example — chained conditions |
| Comparison operators | `==`, `!=`, `<`, `>`, `<=`, `>=` |
| Chained comparisons | `10 < x < 20` — Pythonic, avoids `and` |
| Logical operators | `and`, `or`, `not` |
| Short-circuit | `and` stops at first falsy; `or` stops at first truthy |
| Truthiness | What is falsy in Python |
| `is` / `is not` | Identity check (same object, not just equal value) |
| `in` / `not in` | Membership test |
| Ternary expression | `value_if_true if condition else value_if_false` |
| `match / case` | Python 3.10+ structural pattern matching |

---

## 🧠 Key Concepts & Gotchas

### Chained comparisons — Pythonic!
```python
x = 15
10 < x < 20        # True  — clean Python style
10 < x and x < 20  # True  — equivalent but verbose
```

### Short-circuit evaluation
```python
# 'and' — stops at first falsy value
0 and some_function()    # returns 0, function never called

# 'or' — stops at first truthy value
1 or some_function()     # returns 1, function never called

# Practical: default value pattern
name = ""
display = name or "Anonymous"   # "Anonymous" — name is falsy
```

### Falsy values in Python
```python
# These all evaluate to False in a boolean context:
0, 0.0, 0j        # zero of any numeric type
""                 # empty string
[], {}, set()      # empty collections
None
False
```

### `is` vs `==` — common mistake
```python
a = [1, 2, 3]
b = [1, 2, 3]
a == b    # True  — same value
a is b    # False — different objects in memory

# Use 'is' only for None checks:
if value is None: ...
if value is not None: ...
```

### Ternary expression
```python
status = "adult" if age >= 18 else "minor"

# Nested ternary — use sparingly, hurts readability
sign = "positive" if n > 0 else ("negative" if n < 0 else "zero")
```

### `match / case` (Python 3.10+)
```python
match code:
    case 200:           return "OK"
    case 400:           return "Bad Request"
    case 401 | 403:     return "Auth error"   # OR pattern
    case _:             return "Unknown"      # wildcard (default)

# Structural pattern matching — destructuring
match point:
    case (0, 0):        return "origin"
    case (0, y):        return f"y-axis at {y}"
    case (x, 0):        return f"x-axis at {x}"
    case (x, y):        return f"at ({x}, {y})"
```

---

## 🚀 Run It

```powershell
python if_conditions.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [fundamentals](../README.md)*
