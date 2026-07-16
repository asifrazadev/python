# Iterators

Part of the **Intermediate Python** series. → [Back to intermediate](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **Iterable** | An object capable of returning its members one at a time (e.g. list, tuple, dict, custom classes with `__iter__`). |
| **Iterator** | The object that does the actual iterating. It tracks the state and returns items one-by-one via `__next__`. |
| **`StopIteration`** | The exception raised to signal the end of iteration. |

---

## 🧠 Key Concepts & Gotchas

### Iterables vs Iterators
- An **Iterable** is a container (like a bookshelf). It has an `__iter__` method that gives you a bookmark.
- An **Iterator** is the bookmark. It keeps track of where you are and gives you the next book when you call `next()` on it.

### How a `for` loop works under the hood
```python
# The loop:
for x in obj:
    print(x)

# Is equivalent to:
iterator = iter(obj)
while True:
    try:
        x = next(iterator)
        print(x)
    except StopIteration:
        break
```

### State is stateful
An iterator is exhausted after it traverses all items once. You cannot reset it unless you create a new iterator object.

---

## 🚀 Run It

```powershell
python iterators.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [intermediate](../README.md)*
