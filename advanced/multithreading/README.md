# Multithreading

Part of the **Advanced Python** series. → [Back to advanced](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **Thread** | A lightweight unit of execution within a process. |
| **Concurrency** | Running multiple tasks in overlapping timeframes (ideal for I/O bound tasks). |
| **GIL (Global Interpreter Lock)** | A lock that allows only one thread to execute Python bytecode at a time. |
| **`t.start()`** | Begins thread execution in a separate thread. |
| **`t.join()`** | Blocks the main program until the target thread finishes execution. |

---

## 🧠 Key Concepts & Gotchas

### When to use Multithreading?
- **Use for I/O Bound Tasks**: Web scraping, file downloading, database requests, and network communication.
- **Do NOT use for CPU Bound Tasks**: Math computation, image processing, or heavy loops. (Due to the GIL, multithreading on CPU-bound tasks in Python can actually be *slower* than running them sequentially!).

### Global Interpreter Lock (GIL)
Python's standard implementation (CPython) uses a mutex called the GIL. This ensures only one thread runs Python code at once. Because of this:
- Python threads share memory easily.
- True multi-core execution is not possible with threads; you must use **Multiprocessing** for CPU-bound tasks instead.

---

## 🚀 Run It

```powershell
python multithreading.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [advanced](../README.md)*
