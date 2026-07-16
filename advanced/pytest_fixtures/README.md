# pytest Fixtures

Part of the **Advanced Python** series. → [Back to advanced](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **`@pytest.fixture`** | Decorator used to define a fixture. Provides setup data or resources to tests. |
| **Setup & Teardown** | Code before `yield` runs before the test; code after `yield` runs after the test. |
| **Dependency Injection** | Tests request fixtures by adding them as arguments to test functions. |

---

## 🧠 Key Concepts & Gotchas

### Why use Fixtures?
If multiple test functions need the same mock data, database connection, or API client, you should use a fixture. It avoids repeating setup and teardown code in every single test function.

```python
@pytest.fixture
def sample_data():
    return [1, 2, 3]

def test_sum(sample_data): # dependency injected here
    assert sum(sample_data) == 6
```

### Yield for Teardown
Using `yield` instead of `return` in a fixture allows you to run cleanup code (teardown) after the test completes.
```python
@pytest.fixture
def connection():
    conn = open_connection()
    yield conn                # test executes here
    conn.close()             # runs after the test finishes
```

---

## 🚀 Run It

```powershell
pytest test_fixtures.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [advanced](../README.md)*
