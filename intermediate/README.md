# 🟡 Intermediate Python

> **Goal:** Write idiomatic, reusable, and well-tested Python.
> **Prerequisites:** Complete all scripts in [`../fundamentals/`](../fundamentals/)

---

## 📋 Topics Planned

| # | File | Topic | Key Concepts |
|---|------|-------|-------------|
| 1 | `oop.py` | Object-Oriented Programming | classes, inheritance, `super()`, dunder methods, `@property` |
| 2 | `iterators_generators.py` | Iterators & Generators | `__iter__`/`__next__`, `yield`, `yield from`, `itertools` |
| 3 | `decorators.py` | Decorators | `functools.wraps`, stacked decorators, parametrised decorators |
| 4 | `context_managers.py` | Context Managers | `with`, `__enter__`/`__exit__`, `contextlib` |
| 5 | `comprehensions.py` | Comprehensions | list, dict, set, generator expressions |
| 6 | `regex.py` | Regular Expressions | `re` module, groups, lookaheads, `re.compile` |
| 7 | `testing.py` | Unit Testing | `unittest`, `pytest`, fixtures, mocking |
| 8 | `type_hints.py` | Type Hints | `typing`, `mypy`, generics, `Protocol` |
| 9 | `dataclasses.py` | Dataclasses | `@dataclass`, `field()`, frozen, `__post_init__` |
| 10 | `venvs.py` | Virtual Environments | `venv`, `pip`, `poetry`, `uv` |

---

## 🚀 Running Scripts

```powershell
# Run a single script
python intermediate\oop.py

# Run all scripts
Get-ChildItem intermediate\*.py | ForEach-Object { Write-Host "--- $_ ---"; python $_ }
```

---

*Status: 🔜 Coming soon*
