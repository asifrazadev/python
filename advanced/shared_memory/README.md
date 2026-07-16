# Sharing Data between Processes (Value and Array)

Part of the **Advanced Python** series. → [Back to advanced](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **Process Isolation** | By default, processes do not share variables (modifying a global variable inside a process does not affect the main process). |
| **`multiprocessing.Value`** | A shared memory wrapper for a single primitive value. |
| **`multiprocessing.Array`** | A shared memory wrapper for a 1D array of primitive values. |

---

## 🧠 Key Concepts & Gotchas

### Process Memory Barrier
When you spawn a new process, the operating system copies the parent process's memory. Modifying standard variables in the child process **will not** modify them in the parent.

```python
# THIS DOES NOT WORK:
results = []
p = Process(target=calc, args=(results,))
# results remains empty in the main program!
```

### Shared Memory API
To share data, we must use raw shared memory buffers:
- **`multiprocessing.Value(typecode, value)`**: Typecodes: `'i'` for integer, `'d'` for double (float), `'c'` for char.
- **`multiprocessing.Array(typecode, size_or_initializer)`**: Holds multiple values of the same type.

---

## 🚀 Run It

```powershell
python shared_memory.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [advanced](../README.md)*
