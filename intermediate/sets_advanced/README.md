# Sets and Frozen Sets

Part of the **Intermediate Python** series. → [Back to intermediate](../README.md)

---

## 📖 What's Covered

| Set Type | Mutable? | Hashable (Can be Dict Key / Set Element)? | Syntax |
|----------|----------|-------------------------------------------|--------|
| **Set** | Yes | No | `{"apple", "orange"}` |
| **Frozenset** | No | Yes | `frozenset(["apple", "orange"])` |

---

## 🧠 Key Concepts & Gotchas

### Standard Set vs Frozenset
Normal sets are mutable, which means you can call `.add()`, `.discard()`, `.clear()`.
However, because they are mutable, they cannot be used as:
- Keys in dictionaries.
- Elements inside another set.

To overcome this, Python provides `frozenset`. A `frozenset` is completely immutable. Once created, its elements cannot be changed. This makes it **hashable** and valid for dictionary keys and set elements.

```python
# Normal Set - Throws TypeError: unhashable type: 'set'
# bad_dict = { {"London", "UK"}: "Europe" }

# Frozenset - Works perfectly!
good_dict = { frozenset(["London", "UK"]): "Europe" }
```

---

## 🚀 Run It

```powershell
python sets_advanced.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [intermediate](../README.md)*
