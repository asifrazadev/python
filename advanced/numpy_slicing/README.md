# NumPy Slicing, Stacking, and Boolean Indexing

Part of the **Advanced Python** series. → [Back to advanced](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **2D Slicing** | Accessing sub-matrices using the `a[row_range, col_range]` syntax. |
| **Boolean Indexing** | Filtering arrays using conditional expressions (e.g. `a[a > 5]`). Returns a flat array of matches. |
| **`hstack`** | Stacks arrays horizontally (side-by-side). |
| **`vstack`** | Stacks arrays vertically (top-to-bottom). |

---

## 🧠 Key Concepts & Gotchas

### 2D Slicing Syntax
- `:` means select all items along that dimension.
- `0:2` means select indices 0 and 1 (2 is excluded).

```python
a[:, 2]     # Select all rows, only column index 2
a[1:3, 0:2] # Rows 1 to 2, columns 0 to 1
```

### Stacking Requirements
For stacking to work, the dimensions of the input arrays must align:
- For `vstack`, columns count must match.
- For `hstack`, rows count must match.

---

## 🚀 Run It

```powershell
python numpy_slicing.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [advanced](../README.md)*
