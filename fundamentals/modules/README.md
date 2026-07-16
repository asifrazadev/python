# Modules & Package Managers

Part of the **Python Fundamentals** series. → [Back to fundamentals](../README.md)

---

## 📖 What's Covered

| Section | Key Points |
|---------|-----------|
| Import styles | `import`, `from ... import`, `as` alias, star import (avoid) |
| `__name__` | `if __name__ == "__main__"` guard |
| stdlib highlights | `os`, `sys`, `pathlib`, `random`, `datetime`, `json`, `collections`, `itertools` |
| Package managers | `pip`, `poetry`, `uv` — install, add, run |

---

## 🧠 Key Concepts & Gotchas

### Import styles
```python
import math                          # access as math.pi
from os import path                  # import one name
from os.path import join, exists     # import multiple names
from datetime import datetime as dt  # alias
from math import *                   # star import — avoid (pollutes namespace)
```

### `if __name__ == "__main__"` guard
```python
# In mymodule.py:
def helper():
    return 42

if __name__ == "__main__":
    # Only runs when this file is executed directly
    # NOT when imported by another module
    print(helper())
```

### Key stdlib modules

#### `os` — OS interface
```python
import os
os.getcwd()               # current working directory
os.listdir(".")           # list directory contents
os.makedirs("dir", exist_ok=True)  # create directory
os.environ.get("HOME")    # environment variable
os.cpu_count()            # number of CPU cores
```

#### `pathlib` — modern file paths (prefer over `os.path`)
```python
from pathlib import Path
p = Path("data") / "file.txt"   # cross-platform path joining
p.exists()
p.read_text()
p.parent        # parent directory
p.stem          # filename without extension
p.suffix        # ".txt"
Path.home()     # home directory
Path(__file__).parent  # directory of current script
```

#### `sys`
```python
import sys
sys.argv        # command-line arguments
sys.exit(0)     # exit with code
sys.path        # module search path
sys.version     # Python version string
```

#### `random`
```python
import random
random.seed(42)                     # reproducible results
random.random()                     # float in [0.0, 1.0)
random.randint(1, 100)              # int in [1, 100]
random.choice(["a","b","c"])        # random element
random.shuffle(lst)                 # in-place shuffle
random.sample(range(100), 5)       # 5 unique items
```

#### `datetime`
```python
from datetime import datetime, date, timedelta
datetime.now()
date.today()
date.today() + timedelta(days=7)    # one week from now
datetime.now().strftime("%Y-%m-%d") # format as string
datetime.strptime("2024-01-15", "%Y-%m-%d")  # parse string
```

### Package managers

| Tool | Install | Add Package | Virtual Env |
|------|---------|-------------|-------------|
| **pip** | bundled | `pip install requests` | `python -m venv .venv` |
| **poetry** | `pip install poetry` | `poetry add requests` | auto-managed |
| **uv** | `pip install uv` | `uv add requests` | auto-managed |

```powershell
# pip
pip install requests
pip freeze > requirements.txt
pip install -r requirements.txt

# uv (fastest)
uv init myproject
uv add requests
uv run python main.py
```

---

## 🚀 Run It

```powershell
python modules.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [fundamentals](../README.md)*
