# Strings

Part of the **Python Fundamentals** series. → [Back to fundamentals](../README.md)

---

## 📖 What's Covered

| Section | Key Points |
|---------|-----------|
| Literals | Single, double, triple quotes, raw strings `r"..."` |
| Escape sequences | `\n`, `\t`, `\\`, `\"` |
| F-strings (3.6+) | `f"{name}"`, format spec `:.4f`, `{val!r}`, debug `{expr=}` |
| Common methods | `strip`, `lower`, `upper`, `replace`, `split`, `join`, `title` |
| Searching | `find`, `count`, `startswith`, `endswith`, `in` |
| Slicing | `s[start:stop:step]`, `s[::-1]` to reverse |
| Formatting styles | `%`, `.format()`, f-strings |
| Immutability | Strings cannot be modified in-place |
| `ord` / `chr` | Character ↔ Unicode code point |

---

## 🧠 Key Concepts & Gotchas

### Strings are immutable
```python
word = "hello"
word[0] = "H"       # TypeError!
word = "H" + word[1:]  # create a new string instead
```

### Raw strings — backslash is literal
```python
path = r"C:\Users\name\new_folder"   # no escape processing
regex = r"\d+\.\d+"                  # great for regex patterns
```

### F-string format specifiers
```python
f"{3.14159:.2f}"       # '3.14'          — 2 decimal places
f"{'hello':>10}"       # '     hello'    — right-align, width 10
f"{'hello':<10}"       # 'hello     '    — left-align
f"{'hello':^10}"       # '  hello   '    — center
f"{1_000_000:,}"       # '1,000,000'     — thousands separator
f"{255:#x}"            # '0xff'          — hex with prefix
f"{value!r}"           # repr() of value — useful for debugging
f"{value!s}"           # str() of value
f"{expr=}"             # prints 'expr=result' — debug shorthand (3.8+)
```

### Slicing
```python
s = "Hello, Python!"
s[0]        # 'H'       — first char
s[-1]       # '!'       — last char
s[0:5]      # 'Hello'   — start:stop (stop exclusive)
s[7:]       # 'Python!' — from index 7 to end
s[:5]       # 'Hello'   — from start to index 5
s[::-1]     # '!nohtyP ,olleH' — reverse
s[::2]      # every second char
```

### `split` and `join` are inverses
```python
csv = "apple,banana,cherry"
parts = csv.split(",")            # ['apple', 'banana', 'cherry']
joined = " | ".join(parts)        # 'apple | banana | cherry'
```

### `find` vs `index`
```python
s.find("fox")    # returns -1 if not found (safe)
s.index("fox")   # raises ValueError if not found
```

### String multiplication
```python
"-" * 40    # '----------------------------------------'
"ha" * 3    # 'hahaha'
```

---

## 🚀 Run It

```powershell
python strings.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [fundamentals](../README.md)*
