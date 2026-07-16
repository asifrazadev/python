# Dictionaries

Part of the **Python Fundamentals** series. → [Back to fundamentals](../README.md)

---

## 📖 What's Covered

| Section | Key Points |
|---------|-----------|
| Creation | `{}`, `dict()`, `dict.fromkeys()` |
| Access | `d[key]`, `d.get(key, default)` |
| Mutation | add/update with `d[k]=v`, `del d[k]`, `pop()`, `setdefault()` |
| Methods | `keys()`, `values()`, `items()`, `update()` |
| Iteration | `for k in d`, `for k, v in d.items()` |
| Comprehensions | `{k: v for k, v in ...}` |
| Merging | `{**d1, **d2}`, `d1 \| d2` (3.9+), `d1 \|= d2` |
| Nested dicts | safe access with `.get()` chaining |
| `defaultdict` | auto-creates missing keys |
| `Counter` | count occurrences, `most_common()` |
| Sorting | `sorted(d.items(), key=...)` |

---

## 🧠 Key Concepts & Gotchas

### `d[key]` vs `d.get(key)`
```python
d = {"name": "Alice"}
d["age"]            # KeyError if missing!
d.get("age")        # None if missing — safe
d.get("age", 0)     # 0 if missing — with default
```

### `setdefault` — set only if key is absent
```python
d.setdefault("score", 100)   # adds score=100 only if "score" not in d
d.setdefault("score", 999)   # ignored — "score" already exists
```

### Merging dicts (3.9+)
```python
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}
merged = d1 | d2      # {"a":1, "b":99, "c":3} — d2 wins on conflicts
d1 |= d2              # in-place update
```

### `defaultdict` — no more key checks
```python
from collections import defaultdict
word_count = defaultdict(int)
for word in "apple banana apple".split():
    word_count[word] += 1   # no KeyError — missing keys default to int() = 0
```

### `Counter` — count anything
```python
from collections import Counter
c = Counter("mississippi")
c.most_common(3)   # [('s', 4), ('i', 4), ('p', 2)]
```

### Dict comprehensions
```python
squares  = {x: x**2 for x in range(1, 6)}
filtered = {k: v for k, v in d.items() if v > 5}
inverted = {v: k for k, v in d.items()}   # swap keys and values
```

### Dicts are ordered (Python 3.7+)
Insertion order is preserved — you can rely on iteration order.

### Keys must be hashable
```python
{[1, 2]: "list"}   # TypeError — lists are not hashable
{(1, 2): "tuple"}  # OK — tuples are hashable
```

---

## 🚀 Run It

```powershell
python dictionaries.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [fundamentals](../README.md)*
