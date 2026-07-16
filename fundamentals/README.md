# python-fundamentals

A collection of well-commented Python scripts covering every core concept from the **Complete Python 3 Tutorials for Beginners** playlist. Each file is self-contained and can be run independently.

---

## 📋 Topics Covered

| # | File | Topic | Key Concepts |
|---|------|--------|-------------|
| 1 | [`variables.py`](variables.py) | Variables & Data Types | assignment, multiple assignment, type hints, constants, `id()`, `del` |
| 2 | [`python_numbers.py`](python_numbers.py) | Numbers | int, float, complex, arithmetic operators, `math` module, `decimal`, `fractions`, bitwise ops |
| 3 | [`strings.py`](strings.py) | Strings | literals, escape sequences, f-strings, slicing, common methods, `ord`/`chr` |
| 4 | [`lists.py`](lists.py) | Lists | indexing, mutation, list methods, comprehensions, sorting, copying, nested lists |
| 5 | [`dictionaries.py`](dictionaries.py) | Dictionaries | CRUD, iteration, comprehensions, merging (`|`), `defaultdict`, `Counter` |
| 6 | [`sets.py`](sets.py) | Sets | set operations (union/intersection/difference/symmetric_difference), `frozenset`, comprehensions |
| 7 | [`tuples.py`](tuples.py) | Tuples | immutability, unpacking, `namedtuple`, `typing.NamedTuple`, hashability |
| 8 | [`if_conditions.py`](if_conditions.py) | If Conditions | `if/elif/else`, comparison & logical operators, ternary, `match/case` (3.10+), truthiness |
| 9 | [`for_loops.py`](for_loops.py) | For Loops | `range()`, `enumerate()`, `zip()`, nested loops, `break`/`continue`/`else`, `itertools` |
| 10 | [`functions.py`](functions.py) | Functions | parameters (`*args`/`**kwargs`), closures, decorators, generators, recursion, `lru_cache` |
| 11 | [`lambda_functions.py`](lambda_functions.py) | Lambda Functions | syntax, `map()`/`filter()`/`reduce()`, `sorted()` with `key=`, closures, dispatch dicts |
| 12 | [`modules.py`](modules.py) | Modules & Package Managers | import styles, stdlib highlights, `pip` / `poetry` / `uv` usage guide |
| 13 | [`file_io.py`](file_io.py) | File I/O | read/write/append, modes, `pathlib`, CSV, JSON, binary files, `os.path` |
| 14 | [`exception_handling.py`](exception_handling.py) | Exception Handling | `try/except/else/finally`, custom exceptions, context managers, logging, best practices |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+ (some examples use `match/case` which requires 3.10)
- No external dependencies — all scripts use the standard library only

### Running a Script

```bash
# Clone the repo
git clone https://github.com/<your-username>/python-fundamentals.git
cd python-fundamentals

# Run any script
python variables.py
python numbers.py
python strings.py
# ... etc.
```

### Run All Scripts

```bash
# macOS / Linux
for f in *.py; do echo "--- $f ---"; python "$f"; done

# Windows PowerShell
Get-ChildItem *.py | ForEach-Object { Write-Host "--- $_ ---"; python $_ }
```

---

## 📦 Package Manager Quick Reference

All three major Python package managers are documented in [`modules.py`](modules.py):

| Tool | Install | Add Dependency | Speed |
|------|---------|----------------|-------|
| **pip** | bundled | `pip install pkg` | ⭐⭐ |
| **poetry** | `pip install poetry` | `poetry add pkg` | ⭐⭐ |
| **uv** | `pip install uv` | `uv add pkg` | ⭐⭐⭐ |

---

## 📚 Learning Resources

- [Complete Python 3 Tutorials for Beginners (Full Playlist)](https://www.youtube.com/results?search_query=complete+python+3+tutorial+beginners+full+playlist)
- [Official Python Documentation](https://docs.python.org/3/)
- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [Real Python](https://realpython.com/)

---

## 🗂 Project Structure

```
python-fundamentals/
├── variables.py
├── python_numbers.py
├── strings.py
├── lists.py
├── dictionaries.py
├── sets.py
├── tuples.py
├── if_conditions.py
├── for_loops.py
├── functions.py
├── lambda_functions.py
├── modules.py
├── file_io.py
├── exception_handling.py
└── README.md
```

---

## ✅ Acceptance Criteria

- [x] GitHub repo named `python-fundamentals`
- [x] Each topic has its own `.py` file
- [x] Every file has working code that demonstrates the concept
- [x] Repo has a README listing all topics covered

---

*Built as part of the Python Fundamentals learning track — Videos 1–18.*
