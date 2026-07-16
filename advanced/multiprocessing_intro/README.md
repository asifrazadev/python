# Multiprocessing Introduction

Part of the **Advanced Python** series. → [Back to advanced](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **Process** | An independent program execution unit with its own memory space. |
| **Parallelism** | Executing multiple tasks simultaneously on different CPU cores. |
| **`__name__ == "__main__"`** | Mandatory guard when launching child processes in Windows/macOS. |

---

## 🧠 Key Concepts & Gotchas

### Thread vs Process
- **Threads** share the same memory space. They are blocked by the GIL. Great for I/O tasks.
- **Processes** have separate, isolated memory spaces. Each process runs its own Python interpreter. They bypass the GIL completely and can run in parallel on multiple cores. Great for CPU-bound tasks.

### The Mandatory `__main__` Guard
On Windows and macOS, new processes are started by spawning a fresh Python interpreter which imports your main script. If you don't use the `if __name__ == "__main__":` guard, child processes will recursively spawn copies of themselves, causing your computer to crash!

```python
# MUST DO:
if __name__ == "__main__":
    p = multiprocessing.Process(target=my_func)
    p.start()
```

---

## 🚀 Run It

```powershell
python multiprocessing_intro.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [advanced](../README.md)*
