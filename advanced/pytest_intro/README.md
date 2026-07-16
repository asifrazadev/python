# pytest Introduction

Part of the **Advanced Python** series. → [Back to advanced](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **pytest** | A popular testing framework in Python that simplifies writing unit tests. |
| **`assert`** | Standard Python statement used to verify conditions (throws `AssertionError` if condition is False). |
| **Test discovery** | pytest automatically runs any files named `test_*.py` and any functions named `test_*()`. |

---

## 🧠 Key Concepts & Gotchas

### How pytest works
Unlike standard library `unittest` which requires creating boilerplate classes, pytest is simple and function-based. All you need to do is write functions prefixed with `test_` and use standard `assert` statements.

```python
# To test this:
def add(a, b):
    return a + b

# Write this:
def test_add():
    assert add(2, 3) == 5
```

---

## 🚀 Run It

First install `pytest`:
```powershell
pip install pytest
```

Run tests in this folder:
```powershell
pytest test_intro.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [advanced](../README.md)*
