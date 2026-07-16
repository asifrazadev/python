# Numbers & Math

Part of the **Python Fundamentals** series. → [Back to fundamentals](../README.md)

---

## 📖 What's Covered

| Section | Key Points |
|---------|-----------|
| Integers | Unlimited precision, `0b`/`0o`/`0x` literals, `_` separator |
| Floats | IEEE 754, scientific notation `6.022e23`, `inf`, `nan` |
| Complex | `3 + 4j`, `.real`, `.imag`, `abs()` |
| Arithmetic | `+`, `-`, `*`, `/`, `//`, `%`, `**` |
| Rounding | `round()` (banker's), `math.floor`, `math.ceil`, `math.trunc` |
| `math` module | `pi`, `e`, `sqrt`, `log`, `factorial`, `gcd`, `isclose` |
| Bitwise ops | `&`, `\|`, `^`, `~`, `<<`, `>>` |
| `decimal` | Exact decimal arithmetic (avoids float rounding) |
| `fractions` | Exact rational arithmetic |
| Type conversions | `int()`, `float()`, `bin()`, `oct()`, `hex()` |

---

## 🧠 Key Concepts & Gotchas

### Integer division vs true division
```python
17 / 5   # 3.4   — always returns float (true division)
17 // 5  # 3     — floor division, always rounds down
17 % 5   # 2     — modulo (remainder)
```

### Float precision pitfall
```python
0.1 + 0.2 == 0.3   # False! — float rounding
math.isclose(0.1 + 0.2, 0.3)   # True — correct way to compare
```

### Use `decimal` when precision matters (money, science)
```python
from decimal import Decimal
Decimal("0.1") + Decimal("0.2")   # Decimal('0.3') — exact
```

### Banker's rounding (`round()`)
```python
round(2.5)   # 2 — rounds to nearest EVEN (not always up!)
round(3.5)   # 4
round(3.14159, 2)   # 3.14
```

### Underscore in numeric literals (readability)
```python
big = 1_000_000     # same as 1000000
pi  = 3.141_592_653
```

### Bitwise operators
```python
x = 0b1100   # 12
y = 0b1010   # 10
x & y  # 0b1000 = 8   (AND)
x | y  # 0b1110 = 14  (OR)
x ^ y  # 0b0110 = 6   (XOR)
x << 1 # 0b11000 = 24 (left shift = multiply by 2)
x >> 1 # 0b0110  = 6  (right shift = divide by 2)
```

### `math` highlights
```python
math.gcd(48, 18)     # 6
math.factorial(10)   # 3628800
math.sqrt(2)         # 1.4142135...
math.log(100, 10)    # 2.0
```

---

## 🚀 Run It

```powershell
python python_numbers.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [fundamentals](../README.md)*
