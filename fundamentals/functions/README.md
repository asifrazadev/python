# Functions

Part of the **Python Fundamentals** series. → [Back to fundamentals](../README.md)

---

## 📖 What's Covered

| Section | Key Points |
|---------|-----------|
| Basic `def` | Docstrings, type hints, `return` |
| Parameters | Positional, keyword, defaults, `*args`, `**kwargs`, positional-only `/` (3.8+) |
| Return values | Single, multiple (tuple), `None` |
| Scope (LEGB) | Local → Enclosing → Global → Built-in; `global`, `nonlocal` |
| Closures | Inner function captures enclosing scope variable |
| Decorators | `@logger`, `functools.wraps`, decorator with arguments, stacking |
| Generators | `yield`, generator expressions, `send()` |
| Recursion | Base case + recursive case, `@functools.lru_cache` |
| First-class functions | Functions as arguments, return values, stored in lists |

---

## 🧠 Key Concepts & Gotchas

### Parameter order rule
```python
def f(pos1, pos2, /, normal, *, kw_only, **kwargs):
    pass
#   ^pos-only^  ^regular^  ^kw-only^  ^extras^
```

### `*args` and `**kwargs`
```python
def total(*args):          # any number of positional args → tuple
    return sum(args)

def display(**kwargs):     # any number of keyword args → dict
    for k, v in kwargs.items():
        print(k, v)

total(1, 2, 3, 4)
display(name="Alice", age=30)
```

### ⚠️ Mutable default argument trap
```python
# WRONG — list is shared across all calls!
def append_to(item, lst=[]):
    lst.append(item)
    return lst

# CORRECT — use None as default
def append_to(item, lst=None):
    if lst is None:
        lst = []
    lst.append(item)
    return lst
```

### LEGB scope
```python
x = "global"
def outer():
    x = "enclosing"
    def inner():
        x = "local"
        print(x)   # "local" — innermost wins
    inner()

# Modify outer scopes:
global counter   # modify global variable
nonlocal count   # modify enclosing function variable
```

### Closures
```python
def multiplier(factor):
    def multiply(x):
        return x * factor   # captures 'factor' from enclosing scope
    return multiply

double = multiplier(2)
double(5)   # 10 — 'factor' is remembered even after multiplier() returned
```

### Decorators
```python
import functools

def logger(func):
    @functools.wraps(func)   # preserves __name__, __doc__
    def wrapper(*args, **kwargs):
        print(f"calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"returned {result}")
        return result
    return wrapper

@logger
def add(a, b):
    return a + b
# equivalent to: add = logger(add)
```

### Generators — lazy evaluation
```python
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a          # pauses here, resumes on next()
        a, b = b, a + b

list(fibonacci(10))   # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# Generator expression (memory-efficient)
total = sum(x**2 for x in range(1_000_000))   # never builds the full list
```

### `lru_cache` — memoisation
```python
@functools.lru_cache(maxsize=None)
def fib(n):
    if n < 2: return n
    return fib(n-1) + fib(n-2)

fib(30)              # instant — results cached
fib.cache_info()     # CacheInfo(hits=28, misses=31, ...)
```

---

## 🚀 Run It

```powershell
python functions.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [fundamentals](../README.md)*
