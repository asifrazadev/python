# Multiprocessing Pool (Map Reduce)

Part of the **Advanced Python** series. → [Back to advanced](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **`multiprocessing.Pool`** | Manages a group of worker processes to assign jobs to. |
| **`pool.map()`** | Parallel equivalent of the built-in `map()` function. Distributes input elements to workers. |
| **`pool.close()`** | Tells the pool that no more tasks will be submitted. |
| **`pool.join()`** | Waits for all worker processes to complete. |

---

## 🧠 Key Concepts & Gotchas

### Why use a Pool?
Creating, starting, and joining processes manually for hundreds of small tasks is tedious and has high overhead. A `Pool` creates a fixed number of worker processes (usually matching your system's CPU count) and reuses them to compute values, automatically handling load balancing.

```python
p = Pool()
results = p.map(work_function, input_list)
```

---

## 🚀 Run It

```powershell
python pool_map.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [advanced](../README.md)*
