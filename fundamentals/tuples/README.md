# Tuples

Part of the **Python Fundamentals** series. → [Back to fundamentals](../README.md)

---

## 📖 What's Covered

| Section | Key Points |
|---------|-----------|
| Creation | `(1,2,3)`, `1,2,3` (parens optional), single-item needs trailing comma `(42,)` |
| Indexing & slicing | Same as lists — `t[0]`, `t[-1]`, `t[1:4]`, `t[::-1]` |
| Immutability | Cannot reassign elements — but mutable elements inside CAN change |
| Concatenation | `a + b`, `a * 3` — creates new tuple |
| Unpacking | `x, y = (10, 20)`, starred `first, *middle, last = t` |
| As dict keys | Tuples are hashable → can be used as dict keys |
| Methods | Only `count()` and `index()` |
| `namedtuple` | `collections.namedtuple` — tuple with named fields |
| `typing.NamedTuple` | Class-based, supports type hints and defaults |

---

## 🧠 Key Concepts & Gotchas

### Single-element tuple — trailing comma is REQUIRED
```python
not_a_tuple = (42)    # just parentheses — this is the int 42!
is_a_tuple  = (42,)   # trailing comma makes it a tuple
also_tuple  = 42,     # parens optional
```

### Immutability — elements can't be reassigned
```python
t = (1, 2, 3)
t[0] = 99    # TypeError: 'tuple' object does not support item assignment

# BUT mutable objects inside can still be mutated:
t = ([1, 2], "hello")
t[0].append(3)   # works — the list inside changes, tuple structure doesn't
```

### Unpacking
```python
x, y = (10, 20)                    # basic
first, *middle, last = (1,2,3,4,5) # starred — middle gets [2,3,4]
(a, b), c = (1, 2), 3              # nested unpacking
p, q = q, p                        # swap — uses tuple packing/unpacking
```

### Tuples as dict keys (because they're hashable)
```python
locations = {
    (40.7128, -74.0060): "New York City",
    (51.5074, -0.1278):  "London",
}
print(locations[(40.7128, -74.0060)])  # "New York City"
```

### `namedtuple` — readable, memory-efficient record
```python
from collections import namedtuple
Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
p.x      # 3  — access by name
p[0]     # 3  — still indexable
p._asdict()         # OrderedDict
p._replace(x=10)    # returns new tuple with x=10
```

### `typing.NamedTuple` — with type hints and defaults
```python
import typing
class Vector(typing.NamedTuple):
    x: float
    y: float
    z: float = 0.0   # default value supported

v = Vector(1.0, 2.0)   # z defaults to 0.0
```

### Tuple vs List

| Feature | Tuple | List |
|---------|-------|------|
| Mutable | ✗ No | ✓ Yes |
| Hashable | ✓ Yes | ✗ No |
| Performance | Slightly faster | Slightly slower |
| Use-case | Fixed records, dict keys | Dynamic collections |
| Syntax | `(1, 2, 3)` | `[1, 2, 3]` |

---

## 🚀 Run It

```powershell
python tuples.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [fundamentals](../README.md)*
