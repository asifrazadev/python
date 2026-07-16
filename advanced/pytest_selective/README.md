# pytest - Skip and Selectively Run Tests

Part of the **Advanced Python** series. → [Back to advanced](../README.md)

---

## 📖 What's Covered

| Decorator / Command | Description |
|---------------------|-------------|
| **`@pytest.mark.skip`** | Unconditionally skip a test case. |
| **`@pytest.mark.skipif`** | Skip a test case conditionally (e.g. platform checks). |
| **Custom Markers** | Labeling tests to run subsets of them (e.g., `@pytest.mark.windows`). |
| **`-k` flag** | Run tests by name matching pattern (e.g. `pytest -k total`). |
| **`-m` flag** | Run tests matching specific marker (e.g. `pytest -m windows`). |

---

## 🧠 Key Concepts & Gotchas

### Skip vs Skipif
- Use `skip` for broken or work-in-progress tests:
```python
@pytest.mark.skip(reason="wip")
```
- Use `skipif` when tests only work under specific conditions:
```python
@pytest.mark.skipif(sys.platform == "win32", reason="mac/linux only")
```

### Custom Markers
You can label your tests to group them. Note: pytest will issue a warning if the marker is not registered in your `pytest.ini` config file, but it still executes fine.

---

## 🚀 Run It

Run tests matching "windows" in their name:
```powershell
pytest test_selective.py -k windows
```

Run tests matching custom marker:
```powershell
pytest test_selective.py -m windows
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [advanced](../README.md)*
