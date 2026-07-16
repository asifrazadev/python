# Sharing Data using Queue

Part of the **Advanced Python** series. → [Back to advanced](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **`multiprocessing.Queue`** | A multi-producer, multi-consumer FIFO (First-In, First-Out) queue designed specifically for process communication. |
| **`q.put(item)`** | Inserts an item into the queue. |
| **`q.get()`** | Removes and returns an item from the queue (blocking by default). |

---

## 🧠 Key Concepts & Gotchas

### Multiprocessing Queue vs standard Queue
- **`queue.Queue`** is thread-safe, but it is **not** process-safe. It cannot transfer data between separate OS processes.
- **`multiprocessing.Queue`** uses IPC (Inter-Process Communication) and serializes (pickles) data internally to transmit it safely between processes.

```python
# Thread queue (do NOT use for multiprocessing)
import queue
q = queue.Queue()

# Process queue (DO use for multiprocessing)
import multiprocessing
q = multiprocessing.Queue()
```

---

## 🚀 Run It

```powershell
python process_queue.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [advanced](../README.md)*
