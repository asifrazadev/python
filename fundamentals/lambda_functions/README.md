# Lambda Functions

Part of the **Python Fundamentals** series. → [Back to fundamentals](../README.md)

---

## 📖 What's Covered

| Section | Key Points |
|---------|-----------|
| Syntax | `lambda params: expression` — single expression only |
| With `sorted()` | `key=lambda w: len(w)`, multi-key sort with tuple |
| With `map()` | Apply function to every element — returns iterator |
| With `filter()` | Keep elements where function returns truthy |
| With `reduce()` | Fold a sequence into a single value (`functools.reduce`) |
| In closures | `make_adder`, function composition with `compose()` |
| `lambda` vs `def` | When to use each |
| Practical patterns | `clamp`, dispatch dicts, `defaultdict(lambda: ...)` |

---

## 🧠 Key Concepts & Gotchas

### Syntax
```python
# lambda <params> : <expression>
square = lambda x: x ** 2
add    = lambda x, y: x + y
greet  = lambda name="World": f"Hello, {name}!"

# Immediately invoked (IIFE)
result = (lambda a, b: a * b)(6, 7)   # 42
```

### `sorted()` with `key=`
```python
words = ["banana", "apple", "cherry", "date"]
sorted(words, key=lambda w: len(w))          # by length
sorted(words, key=lambda w: w[-1])           # by last character
sorted(words, key=lambda w: (len(w), w))     # multi-key: length then alpha
```

### `map()` — transform every element
```python
numbers = [1, 2, 3, 4, 5]
list(map(lambda x: x**2, numbers))          # [1, 4, 9, 16, 25]
list(map(str.upper, ["hello", "world"]))    # no lambda needed for methods!
```

### `filter()` — keep matching elements
```python
list(filter(lambda x: x > 0, range(-5, 6)))   # [1, 2, 3, 4, 5]
list(filter(None, [0, 1, "", "hi", None]))      # [1, "hi"] — removes falsy
```

### `reduce()` — fold to single value
```python
from functools import reduce
reduce(lambda acc, x: acc * x, [1,2,3,4,5])   # 120 — product
reduce(lambda a, b: a if a > b else b, [3,1,9,4])  # 9 — max
```

### ⚠️ `lambda` vs `def` — when to use each

| Use `lambda` | Use `def` |
|---|---|
| Short, throwaway, passed inline | Named and reused |
| Single expression | Multiple statements needed |
| `key=` argument to `sorted/map` | Needs docstring |
| Dispatch table value | Needs `return`, `yield`, `raise` |

```python
# lambda OK — short inline key
sorted(employees, key=lambda e: e["salary"])

# def better — complex logic, readable name
def get_sort_key(employee):
    """Sort by salary descending, then name ascending."""
    return (-employee["salary"], employee["name"])
```

### Practical patterns
```python
# Clamp value to range
clamp = lambda x, lo, hi: max(lo, min(hi, x))
clamp(15, 0, 10)   # 10

# Dispatch dict — replaces if/elif chains
ops = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}
ops["*"](6, 7)   # 42

# Nested defaultdict
from collections import defaultdict
nested = defaultdict(lambda: defaultdict(int))
nested["fruits"]["apple"] += 5
```

---

## 🚀 Run It

```powershell
python lambda_functions.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [fundamentals](../README.md)*
