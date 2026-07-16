# NumPy Introduction (Array vs List)

Part of the **Advanced Python** series. → [Back to advanced](../README.md)

---

## 📖 What's Covered

| Feature | Python List | NumPy Array |
|---------|-------------|-------------|
| **Memory** | Stores pointers to objects (heavy memory overhead). | Stores contiguous values directly (very compact). |
| **Speed** | Slow, requires loops for element-wise operations. | Fast, uses compiled C code under the hood (vectorization). |
| **Convenience** | Harder to do element-wise operations (e.g. `L1 + L2` joins lists, doesn't add elements). | Easy element-wise math (e.g. `A1 + A2` adds element-to-element). |

---

## 🧠 Key Concepts & Gotchas

### Why is NumPy faster?
1. **Vectorization**: Operations are run in compiled C code without explicit Python loop structures.
2. **Cache Locality**: Elements are stored right next to each other in memory (contiguous storage), so computer hardware caches them efficiently.

---

## 🚀 Run It

First install `numpy`:
```powershell
pip install numpy
```

Run script:
```powershell
python numpy_intro.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [advanced](../README.md)*
