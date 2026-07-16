# For Loops

Part of the **Python Fundamentals** series. → [Back to fundamentals](../README.md)

---

## 📖 What's Covered

| Section | Key Points |
|---------|-----------|
| Basic `for` | Iterate over list, string, dict |
| `range()` | `range(n)`, `range(start, stop)`, `range(start, stop, step)` |
| `enumerate()` | Get index + value; `start=` parameter |
| `zip()` | Pair up multiple iterables; `zip_longest` for unequal lengths |
| Nested loops | 2-D iteration, multiplication table |
| `break` | Exit loop immediately |
| `continue` | Skip current iteration |
| `for...else` | `else` block runs only if loop completes without `break` |
| Comprehensions | List, dict, set comprehensions, generator expressions |
| `while` loop | Condition-based; do-while emulation |
| `itertools` | `chain`, `cycle`, `repeat`, `count`, `combinations`, `permutations`, `product` |

---

## 🧠 Key Concepts & Gotchas

### `range()` — stop is exclusive
```python
range(5)         # 0, 1, 2, 3, 4  — not 5!
range(2, 8)      # 2, 3, 4, 5, 6, 7
range(0, 10, 2)  # 0, 2, 4, 6, 8  — step of 2
range(10, 0, -1) # 10, 9, 8, ..., 1 — countdown
```

### `enumerate()` — Pythonic index+value
```python
colors = ["red", "green", "blue"]
for i, color in enumerate(colors):           # 0-based
    print(i, color)
for i, color in enumerate(colors, start=1):  # 1-based
    print(i, color)
```

### `zip()` — stops at shortest
```python
names  = ["Alice", "Bob", "Charlie"]
scores = [95, 87, 92]
for name, score in zip(names, scores):
    print(name, score)

# Equal-length guarantee — use zip_longest:
from itertools import zip_longest
list(zip_longest([1, 2], ["a","b","c"], fillvalue=None))
# [(1,'a'), (2,'b'), (None,'c')]
```

### `for...else` — rare but powerful
```python
# else runs ONLY if the loop did NOT hit a break
for n in numbers:
    for d in range(2, n):
        if n % d == 0:
            break        # not prime — skip else
    else:
        print(f"{n} is prime")   # only runs if inner loop completed
```

### `break` vs `continue`
```python
for n in range(10):
    if n == 5:
        break       # stops entire loop
    if n % 2 == 0:
        continue    # skips to next iteration
    print(n)        # prints odd numbers < 5
```

### Comprehensions — prefer over map/filter
```python
squares     = [x**2 for x in range(1, 11)]
evens       = [x for x in range(20) if x % 2 == 0]
flat        = [x for row in [[1,2],[3,4]] for x in row]  # flatten
dict_comp   = {k: v for k, v in zip("abc", [1,2,3])}
set_comp    = {x % 5 for x in range(20)}
gen_expr    = sum(x**2 for x in range(1000))  # memory-efficient, no list created
```

### `itertools` highlights
```python
import itertools
itertools.chain([1,2], [3,4], [5])          # flatten iterables
itertools.cycle("ABC")                       # infinite: A B C A B C ...
itertools.repeat(0, 4)                       # [0, 0, 0, 0]
itertools.combinations("ABCD", 2)            # all 2-combos
itertools.permutations("ABC", 2)             # all 2-perms
itertools.product([0,1], repeat=3)           # Cartesian product (binary combos)
```

---

## 🚀 Run It

```powershell
python for_loops.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [fundamentals](../README.md)*
