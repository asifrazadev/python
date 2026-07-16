# Exception Handling

Part of the **Python Fundamentals** series. → [Back to fundamentals](../README.md)

---

## 📖 What's Covered

| Section | Key Points |
|---------|-----------|
| `try / except` | Catch specific errors; `as e` to inspect |
| Multiple `except` | Different handlers per error type; tuple grouping |
| `try / except / else / finally` | `else` runs if no exception; `finally` always runs |
| `raise` | Re-raise, raise with message, raise from |
| Custom exceptions | Class inheriting `Exception` |
| Exception hierarchy | `BaseException` → `Exception` → specific errors |
| Context managers | `with`, `contextlib.contextmanager`, `suppress` |
| Logging | `logging` module — prefer over `print` for errors |
| Best practices | What to do and avoid |

---

## 🧠 Key Concepts & Gotchas

### Full `try` block structure
```python
try:
    result = risky_operation()
except ValueError as e:
    print(f"Bad value: {e}")       # specific error
except (TypeError, KeyError) as e:
    print(f"Type/Key error: {e}")  # multiple in one clause
except Exception as e:
    print(f"Unexpected: {e}")      # catch-all (avoid if possible)
else:
    print("Success!", result)      # runs ONLY if NO exception occurred
finally:
    print("Always runs")           # cleanup — file close, DB disconnect, etc.
```

### `else` — often forgotten but useful
```python
try:
    data = fetch_data()
except NetworkError:
    data = default_data
else:
    process(data)   # only runs if fetch succeeded — cleaner than putting it in try
```

### `raise` — re-raise and chaining
```python
try:
    int("bad")
except ValueError:
    raise                           # re-raise same exception

raise ValueError("Custom message")  # raise new exception

# Exception chaining — preserve original context
try:
    connect_to_db()
except ConnectionError as e:
    raise RuntimeError("DB unavailable") from e
```

### Custom exceptions
```python
class ValidationError(Exception):
    """Raised when input validation fails."""
    def __init__(self, field, message):
        self.field = field
        super().__init__(f"{field}: {message}")

raise ValidationError("email", "invalid format")
```

### Exception hierarchy (most common)
```
BaseException
├── SystemExit          ← sys.exit()
├── KeyboardInterrupt   ← Ctrl+C
└── Exception           ← catch this, not BaseException
    ├── ValueError      ← wrong value type/range
    ├── TypeError       ← wrong type
    ├── KeyError        ← dict key missing
    ├── IndexError      ← list index out of range
    ├── AttributeError  ← object has no attribute
    ├── FileNotFoundError
    ├── ZeroDivisionError
    ├── RuntimeError
    └── StopIteration   ← end of iterator
```

### Context managers
```python
# Custom context manager with decorator
from contextlib import contextmanager

@contextmanager
def managed_resource():
    resource = acquire()
    try:
        yield resource         # code inside 'with' block runs here
    finally:
        release(resource)      # always runs

with managed_resource() as r:
    use(r)

# suppress — silence specific exceptions
from contextlib import suppress
with suppress(FileNotFoundError):
    os.remove("maybe_exists.txt")   # no crash if file missing
```

### Logging instead of print
```python
import logging
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")

try:
    result = 10 / 0
except ZeroDivisionError:
    logging.error("Division by zero", exc_info=True)   # includes traceback
```

### ✅ Best practices
```python
# DO: catch specific exceptions
except ValueError: ...

# AVOID: bare except — catches SystemExit and KeyboardInterrupt too!
except: ...

# AVOID: catching Exception silently
except Exception:
    pass   # swallows the error — very hard to debug

# DO: log or re-raise if you catch broadly
except Exception as e:
    logging.error(f"Unexpected: {e}", exc_info=True)
    raise
```

---

## 🚀 Run It

```powershell
python exception_handling.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [fundamentals](../README.md)*
