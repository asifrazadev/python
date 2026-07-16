# List, Set, and Dict Comprehensions

Part of the **Intermediate Python** series. → [Back to intermediate](../README.md)

---

## 📖 What's Covered

| Type | Syntax | Result |
|------|--------|--------|
| **List Comprehension** | `[expr for item in iterable if cond]` | Creates a new list |
| **Set Comprehension** | `{expr for item in iterable if cond}` | Creates a new set (unique items) |
| **Dict Comprehension** | `{k_expr: v_expr for item in iterable if cond}` | Creates a new dictionary |

---

## 🧠 Key Concepts & Gotchas

### Readability vs Compactness
Comprehensions are highly Pythonic and make code shorter, but you shouldn't nest them too deeply, or they will hurt readability.

```python
# GOOD: Clean and readable
evens = [x for x in range(10) if x % 2 == 0]

# BAD: Hard to read and debug
matrix = [[1, 2], [3, 4]]
flattened = [val for row in matrix for val in row if val > 2]
```

### Zipping lists for Dict Comprehensions
```python
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {k: v for k, v in zip(keys, values)}
```

---

## 🚀 Run It

```powershell
python comprehensions.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [intermediate](../README.md)*
