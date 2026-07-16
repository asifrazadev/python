# NumPy nditer

Part of the **Advanced Python** series. → [Back to advanced](../README.md)

---

## 📖 What's Covered

| Concept / Flag | Description |
|----------------|-------------|
| **`np.nditer`** | An efficient multidimensional iterator object to iterate over arrays. |
| **`order` flag** | `'C'` order follows standard C memory layout (row-by-row); `'F'` order follows Fortran style (column-by-column). |
| **`op_flags=['readwrite']`** | Tells the iterator that elements will be read and modified in-place using `x[...] = new_value`. |

---

## 🧠 Key Concepts & Gotchas

### Performance Advantages
Standard nested loops (e.g. `for row in a: for col in row:`) are slow in Python because they require many interpreter calls. `np.nditer` handles high-dimensional iterating efficiently in compiled C.

### Modifying in-place syntax
To modify elements during iteration, you must use the `x[...]` syntax to perform assignment inside the array buffer. Using just `x = x * x` only modifies the local variable reference, not the array!

```python
# CORRECT:
for x in np.nditer(a, op_flags=['readwrite']):
    x[...] = x * x
```

---

## 🚀 Run It

```powershell
python numpy_nditer.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [advanced](../README.md)*
