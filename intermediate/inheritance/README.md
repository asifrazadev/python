# Inheritance

Part of the **Intermediate Python** series. → [Back to intermediate](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **Parent Class** | The base class whose properties and methods are inherited. |
| **Child Class** | The subclass that inherits from the parent class. |
| **`super()`** | Built-in function to call the parent class's constructor or methods. |
| **Method Overriding** | Defining a method in a child class with the same name as one in the parent class to change its behavior. |

---

## 🧠 Key Concepts & Gotchas

### Benefits of Inheritance
1. **Code Reusability**: Common code goes in the parent class.
2. **Extensibility**: Subclasses can add specific features (like `open_sunroof` on `Car` but not `Vehicle`).

### Using `super()`
Always call `super().__init__(...)` in the subclass constructor to ensure the base class is properly initialized.
```python
class Car(Vehicle):
    def __init__(self, name, fuel_type, doors):
        super().__init__(name, fuel_type)  # Call parent constructor
        self.doors = doors
```

### Method Overriding
If a child class defines a method that already exists in the parent class, the child's version is executed.
```python
class Motorcycle(Vehicle):
    def start_engine(self):
        print("Roar!")  # Overrides Vehicle's start_engine()
```

---

## 🚀 Run It

```powershell
python inheritance.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [intermediate](../README.md)*
