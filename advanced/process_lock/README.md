# Multiprocessing Lock

Part of the **Advanced Python** series. → [Back to advanced](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **Race Condition** | A bug where multiple processes access/modify shared data concurrently, causing unpredictable results. |
| **Lock** | A synchronization primitive used to guarantee mutual exclusion (only one process executes the locked block at any time). |
| **Critical Section** | The block of code that accesses shared resources. |

---

## 🧠 Key Concepts & Gotchas

### Race Conditions
When writing:
`balance.value = balance.value + 1`

Under the hood, CPU executes three steps:
1. Read `balance.value` into register.
2. Increment value.
3. Write value back to memory.

If two processes do this simultaneously without synchronization, their updates can overwrite each other.

### Using Lock
You can acquire and release locks manually, or use `with lock:` context managers (highly recommended to prevent deadlocks if an error occurs).

```python
# Context Manager (Safe, auto-releases lock)
with lock:
    shared_var.value += 1
```

---

## 🚀 Run It

```powershell
python process_lock.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [advanced](../README.md)*
