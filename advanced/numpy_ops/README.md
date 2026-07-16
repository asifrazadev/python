# NumPy Basic Array Operations

Part of the **Advanced Python** series. → [Back to advanced](../README.md)

---

## 📖 What's Covered

| Operation / Property | Description |
|----------------------|-------------|
| **`ndim`** | Number of axes/dimensions of the array. |
| **`dtype`** | The data type of the elements inside the array. |
| **`shape`** | A tuple indicating the size in each dimension (e.g., `(rows, columns)`). |
| **`reshape()`** | Changes the shape of the array without modifying its data. |
| **`ravel()`** | Flattens a multi-dimensional array into a 1D array. |
| **Axes (`axis`)** | `axis=0` operates columns-wise, `axis=1` operates row-wise. |

---

## 🧠 Key Concepts & Gotchas

### Axis Operations
- **`axis=0`**: Vertical axis (operates downwards, column-by-column).
- **`axis=1`**: Horizontal axis (operates across, row-by-row).

```python
# Array:
# [[1, 2],
#  [3, 4]]
a.sum(axis=0)  # [4, 6]  (1+3, 2+4)
a.sum(axis=1)  # [3, 7]  (1+2, 3+4)
```

---

## 🚀 Run It

```powershell
python numpy_ops.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [advanced](../README.md)*
