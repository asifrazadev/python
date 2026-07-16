# Sets

Part of the **Python Fundamentals** series. → [Back to fundamentals](../README.md)

---

## 📖 What's Covered

| Section | Key Points |
|---------|-----------|
| Creation | `{1,2,3}`, `set()`, `set("hello")` — `{}` is an empty DICT, not set! |
| Membership | `x in s` — O(1) average, much faster than lists |
| Mutation | `add`, `update`, `discard`, `remove`, `pop`, `clear` |
| Set operations | union `\|`, intersection `&`, difference `-`, symmetric difference `^` |
| In-place ops | `\|=`, `&=`, `-=`, `^=` |
| Subset/superset | `<=`, `>=`, `<`, `>`, `==`, `isdisjoint()` |
| `frozenset` | Immutable set — can be used as dict key or set member |
| Comprehensions | `{expr for x in iterable if cond}` |
| Practical uses | deduplication, fast lookup tables, common-element finding |

---

## 🧠 Key Concepts & Gotchas

### ⚠️ Empty set — common mistake
```python
empty_dict = {}      # this is a dict!
empty_set  = set()   # this is the correct empty set
```

### Sets are UNORDERED — no indexing
```python
s = {3, 1, 2}
s[0]   # TypeError — no indexing on sets
```

### `discard` vs `remove`
```python
s.discard(99)   # safe — no error if element missing
s.remove(99)    # raises KeyError if element missing
```

### Set operations — operator vs method
```python
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

A | B   # {1,2,3,4,5,6,7,8}  union         — in A or B
A & B   # {4, 5}              intersection  — in A AND B
A - B   # {1, 2, 3}           difference    — in A but NOT in B
A ^ B   # {1,2,3,6,7,8}      sym.diff      — in A or B, but NOT both
```

### `frozenset` — immutable, hashable
```python
fs = frozenset([1, 2, 3])
# fs.add(4)      # AttributeError — immutable
nested = {frozenset([1,2]), frozenset([3,4])}  # sets of frozensets is valid
```

### Practical patterns
```python
# Deduplicate a list (order not preserved)
unique = list(set([3, 1, 4, 1, 5, 9, 2, 6, 5]))

# Order-preserving dedup
unique_ordered = list(dict.fromkeys([3, 1, 4, 1, 5]))

# Fast membership lookup (better than list for large collections)
STOP_WORDS = {"a", "an", "the", "is"}
words = "the cat is here".split()
filtered = [w for w in words if w not in STOP_WORDS]

# Common elements between two lists
common = set([1,2,3,4]) & set([3,4,5,6])   # {3, 4}
```

---

## 🚀 Run It

```powershell
python sets.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [fundamentals](../README.md)*
