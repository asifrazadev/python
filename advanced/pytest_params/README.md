# pytest Parameters (Parametrize)

Part of the **Advanced Python** series. → [Back to advanced](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **`@pytest.mark.parametrize`** | Decorator used to run a single test function multiple times with different sets of arguments. |
| **Test Matrix** | Specifying input parameters and the expected output in a compact table format. |

---

## 🧠 Key Concepts & Gotchas

### Why use Parametrize?
If you have 10 different inputs to test, you don't need to write 10 separate test functions or use a loop inside a test (which stops on the first failure). Parametrize runs each input as an **independent test run**, showing you exactly which cases passed and which ones failed.

```python
@pytest.mark.parametrize(
    "x, y, result",
    [
        (1, 2, 3),
        (5, 5, 10)
    ]
)
def test_add(x, y, result):
    assert x + y == result
```

---

## 🚀 Run It

```powershell
pytest test_params.py -v
```
*(The `-v` verbose flag prints each input set as a separate line item!)*

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [advanced](../README.md)*
