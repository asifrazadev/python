# Lists

Part of the **Python Fundamentals** series. → [Back to fundamentals](../README.md)

---

## 📖 What's Covered

| Section | Key Points |
|---------|-----------|
| Creation | `[]`, `list(range(...))`, mixed types |
| Indexing & slicing | `lst[0]`, `lst[-1]`, `lst[2:5]`, `lst[::2]` |
| Methods | `append`, `insert`, `extend`, `pop`, `remove`, `sort`, `reverse`, `index`, `count`, `copy`, `clear` |
| `sorted()` | Non-mutating sort, `key=`, `reverse=` |
| Comprehensions | `[expr for x in iterable if cond]` |
| Copying pitfalls | alias vs shallow copy vs `deepcopy` |
| Nested lists | 2-D matrices, transposing |
| Builtins | `len`, `min`, `max`, `sum`, `any`, `all`, `enumerate`, `zip` |

---

## 🧠 Key Concepts & Gotchas

### `append` vs `extend` vs `insert`
```python
lst = [1, 2, 3]
lst.append(4)        # [1, 2, 3, 4]       — adds ONE item
lst.extend([5, 6])   # [1, 2, 3, 4, 5, 6] — adds each item from iterable
lst.insert(0, 0)     # [0, 1, 2, 3, 4, 5, 6] — insert at index
```

### `remove` vs `pop`
```python
lst.remove("apple")  # removes first occurrence by VALUE — ValueError if missing
lst.pop()            # removes & returns LAST item
lst.pop(0)           # removes & returns item at index 0
```

### `sort()` mutates; `sorted()` returns new list
```python
nums = [3, 1, 4, 1, 5]
nums.sort()                          # mutates in-place, returns None
new = sorted(nums, reverse=True)     # returns new list, original unchanged
```

### Sorting with a key
```python
words = ["banana", "apple", "cherry"]
sorted(words, key=len)               # by string length
sorted(words, key=str.lower)         # case-insensitive
```

### ⚠️ Copying pitfall — alias vs copy
```python
original = [1, 2, 3]
alias   = original           # SAME object — mutating alias mutates original!
shallow = original.copy()    # independent copy (but nested objects still shared)
import copy
deep    = copy.deepcopy([[1, 2], [3, 4]])  # fully independent
```

### List comprehensions
```python
squares    = [x**2 for x in range(1, 11)]
evens      = [x for x in range(20) if x % 2 == 0]
flat       = [val for row in [[1,2],[3,4]] for val in row]   # flatten 2D
```

### Useful builtins
```python
any(x > 8 for x in [4, 1, 9])   # True  — at least one satisfies
all(x > 0 for x in [4, 1, 9])   # True  — all satisfy
list(enumerate(['a','b'], start=1))  # [(1, 'a'), (2, 'b')]
list(zip([1,2,3], ['a','b','c']))    # [(1,'a'), (2,'b'), (3,'c')]
```

---

## 🚀 Run It

```powershell
python lists.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [fundamentals](../README.md)*
