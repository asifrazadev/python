# 🔴 Advanced Python

> **Goal:** Master Python internals, concurrency, and high-performance patterns.
> **Prerequisites:** Complete all scripts in [`../intermediate/`](../intermediate/)

---

## 📋 Topics Planned

| # | File | Topic | Key Concepts |
|---|------|-------|-------------|
| 1 | `async_io.py` | Async I/O | `asyncio`, `async/await`, `aiohttp`, event loop |
| 2 | `concurrency.py` | Concurrency & Parallelism | `threading`, `multiprocessing`, `concurrent.futures`, GIL |
| 3 | `metaclasses.py` | Metaclasses | `type`, `__new__`, `__init_subclass__`, class decorators |
| 4 | `descriptors.py` | Descriptors & `__slots__` | `__get__`/`__set__`/`__delete__`, `__slots__`, memory layout |
| 5 | `memory_profiling.py` | Memory & Performance | `tracemalloc`, `cProfile`, `timeit`, `line_profiler` |
| 6 | `c_extensions.py` | C Extensions | `ctypes`, `cffi`, `cython` basics |
| 7 | `packaging.py` | Python Packaging | `pyproject.toml`, `setuptools`, publishing to PyPI |
| 8 | `design_patterns.py` | Design Patterns | Singleton, Factory, Observer, Strategy in Python |
| 9 | `cli_tools.py` | CLI Tools | `argparse`, `click`, `typer`, rich output |
| 10 | `web_scraping.py` | Web Scraping | `httpx`, `BeautifulSoup`, `playwright` |

---

## 🚀 Running Scripts

```powershell
# Run a single script
python advanced\async_io.py

# Run all scripts
Get-ChildItem advanced\*.py | ForEach-Object { Write-Host "--- $_ ---"; python $_ }
```

---

*Status: 🔜 Coming soon*
