# Multiple Inheritance

Part of the **Intermediate Python** series. → [Back to intermediate](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **Multiple Inheritance** | A subclass inheriting attributes and methods from more than one parent class. |
| **MRO (Method Resolution Order)** | The order in which Python searches for a method in a class hierarchy. |
| **`__mro__` attribute** | A tuple of classes that Python inspects when looking for methods. |

---

## 🧠 Key Concepts & Gotchas

### Definition
Unlike languages like Java or C# which restrict multiple class inheritance, Python allows a class to inherit from multiple parent classes.
```python
class Child(Father, Mother):
    pass
```

### Method Resolution Order (MRO)
When a method is called, Python searches the classes in a specific sequence. For a child class `C(A, B)`, it searches:
1. The class `C` itself.
2. The first parent class `A` (and its ancestors).
3. The second parent class `B` (and its ancestors).
4. The base object class.

You can inspect this order using the `__mro__` attribute or `.mro()` method:
```python
print(Child.__mro__)
```

---

## 🚀 Run It

```powershell
python multiple_inheritance.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [intermediate](../README.md)*
