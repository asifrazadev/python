# 🐍 Python Notes

Personal Python learning notes — from absolute beginner to advanced.
Each level lives in its own folder with its own README.

---

## 🗺️ Learning Roadmap

| Level | Folder | Status | Description |
|-------|--------|--------|-------------|
| 🟢 Beginner | [`fundamentals/`](fundamentals/) | ✅ Active | Core syntax, built-in types, control flow, functions, modules, file I/O |
| 🟡 Intermediate | `intermediate/` | 🔜 Coming soon | OOP, iterators, generators, decorators, context managers, testing |
| 🔴 Advanced | `advanced/` | 🔜 Coming soon | Async/await, metaclasses, descriptors, C extensions, performance |

---

## 📁 Folder Structure

```
python/
├── fundamentals/           # 🟢 Beginner — 14 scripts, core concepts
│   ├── variables.py
│   ├── python_numbers.py
│   ├── strings.py
│   ├── lists.py
│   ├── dictionaries.py
│   ├── sets.py
│   ├── tuples.py
│   ├── if_conditions.py
│   ├── for_loops.py
│   ├── functions.py
│   ├── lambda_functions.py
│   ├── modules.py
│   ├── file_io.py
│   ├── exception_handling.py
│   └── README.md
│
├── intermediate/           # 🟡 Coming soon
│   └── README.md
│
├── advanced/               # 🔴 Coming soon
│   └── README.md
│
├── .gitignore
└── README.md               ← you are here
```

---

## 🟢 Beginner — `fundamentals/`

> **Goal:** Understand Python syntax and the standard library basics.

| # | File | Topic |
|---|------|-------|
| 1 | `variables.py` | Variables & Data Types |
| 2 | `python_numbers.py` | Numbers & Math |
| 3 | `strings.py` | Strings |
| 4 | `lists.py` | Lists |
| 5 | `dictionaries.py` | Dictionaries |
| 6 | `sets.py` | Sets |
| 7 | `tuples.py` | Tuples |
| 8 | `if_conditions.py` | If Conditions |
| 9 | `for_loops.py` | For Loops |
| 10 | `functions.py` | Functions |
| 11 | `lambda_functions.py` | Lambda Functions |
| 12 | `modules.py` | Modules & Package Managers |
| 13 | `file_io.py` | File I/O |
| 14 | `exception_handling.py` | Exception Handling |

→ See [`fundamentals/README.md`](fundamentals/README.md) for full details.

---

## 🟡 Intermediate — `intermediate/` *(coming soon)*

> **Goal:** Write idiomatic, reusable, and well-tested Python.

Planned topics:
- Object-Oriented Programming (classes, inheritance, dunder methods)
- Iterators & Generators (`yield`, `itertools`)
- Decorators (functools, custom decorators)
- Context Managers (`with` statement, `contextlib`)
- Comprehensions (list, dict, set, generator)
- Regular Expressions (`re`)
- Unit Testing (`unittest`, `pytest`)
- Virtual Environments & Dependency Management
- Type Hints & `mypy`
- `dataclasses` & `attrs`

---

## 🔴 Advanced — `advanced/` *(coming soon)*

> **Goal:** Deep Python internals and high-performance patterns.

Planned topics:
- Async I/O (`asyncio`, `aiohttp`)
- Concurrency & Parallelism (`threading`, `multiprocessing`)
- Metaclasses & Class Decorators
- Descriptors & `__slots__`
- Memory Management & Profiling
- C Extensions & `ctypes`
- Python Packaging (`pyproject.toml`, publishing to PyPI)
- Design Patterns in Python
- CLI Tools (`argparse`, `click`, `typer`)
- Web Scraping (`httpx`, `BeautifulSoup`, `playwright`)

---

## ⚙️ Requirements

- Python **3.10+** (some scripts use `match/case`)
- No external dependencies for `fundamentals/` — stdlib only
- Later levels may introduce third-party packages (documented per folder)

---

## 🚀 Running Scripts

```powershell
# Run a single script
python fundamentals\variables.py

# Run all scripts in a level
Get-ChildItem fundamentals\*.py | ForEach-Object { Write-Host "--- $_ ---"; python $_ }
```

---

*Learning track — ongoing. Updated as new levels are added.*
