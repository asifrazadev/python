# Class and Objects (OOP Basics)

Part of the **Intermediate Python** series. → [Back to intermediate](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **Class** | A blueprint or template for creating objects. |
| **Object** | An instance of a class containing real values. |
| **`__init__`** | The constructor method, automatically called when creating a new object. |
| **`self`** | Represents the specific instance of the class you are currently working with. |
| **Methods** | Functions defined inside a class that operate on the object's data. |

---

## 🧠 Key Concepts & Gotchas

### Class vs Object
A class is like an architectural drawing (blueprint). An object is the actual house built from that blueprint.

```python
class Human:     # Blueprint
    pass

tom = Human()    # Actual object (instance)
```

### The role of `self`
Every instance method must take `self` as its first parameter. Python automatically passes the object itself as this parameter when you call the method.
```python
# You write:
tom.speaks()

# Under the hood, Python executes:
Human.speaks(tom)
```

### The `__init__` Constructor
Used to initialize the object's attributes.
```python
class Human:
    def __init__(self, name, occupation):
        self.name = name                 # Instance variable
        self.occupation = occupation     # Instance variable
```

---

## 🚀 Run It

```powershell
python oop.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [intermediate](../README.md)*
