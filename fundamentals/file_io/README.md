# File I/O

Part of the **Python Fundamentals** series. → [Back to fundamentals](../README.md)

---

## 📖 What's Covered

| Section | Key Points |
|---------|-----------|
| Writing text | `open(path, "w")`, `write()`, `writelines()` |
| Appending | `open(path, "a")` |
| Reading text | `read()`, `readline()`, `readlines()`, line-by-line iteration |
| Context manager | `with open(...) as f:` — auto-closes file |
| File modes | `r`, `w`, `a`, `r+`, `b` (binary), `x` (exclusive create) |
| `pathlib` | `Path.read_text()`, `Path.write_text()`, `Path.glob()` |
| CSV | `csv.reader`, `csv.writer`, `csv.DictReader`, `csv.DictWriter` |
| JSON | `json.dump`, `json.load`, `json.dumps`, `json.loads` |
| Binary files | `"rb"`, `"wb"` modes, bytearray, struct |
| `os.path` | `exists`, `isfile`, `isdir`, `getsize`, `splitext` |

---

## 🧠 Key Concepts & Gotchas

### Always use `with` — auto-closes the file
```python
# BAD — file may not close if an exception occurs
f = open("data.txt", "r")
content = f.read()
f.close()

# GOOD — context manager guarantees close
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

### File modes
| Mode | Meaning |
|------|---------|
| `"r"` | Read (default) — error if file missing |
| `"w"` | Write — creates or OVERWRITES |
| `"a"` | Append — creates or adds to end |
| `"x"` | Exclusive create — error if file exists |
| `"r+"` | Read + write, file must exist |
| `"rb"` | Binary read |
| `"wb"` | Binary write |

### Reading strategies
```python
with open("file.txt", encoding="utf-8") as f:
    content = f.read()           # entire file as one string
    lines = f.readlines()        # list of lines (includes \n)
    line = f.readline()          # one line at a time

# Most Pythonic — iterate line by line (memory-efficient)
with open("big_file.txt") as f:
    for line in f:
        process(line.strip())
```

### Always specify encoding
```python
open("file.txt", "r", encoding="utf-8")   # explicit is better
# Default encoding varies by OS — can cause bugs on Windows!
```

### CSV
```python
import csv

# Write
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age"])
    writer.writeheader()
    writer.writerow({"name": "Alice", "age": 30})

# Read
with open("data.csv", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        print(row["name"], row["age"])
```

### JSON
```python
import json

data = {"name": "Alice", "scores": [95, 87, 92]}

# Write to file
with open("data.json", "w") as f:
    json.dump(data, f, indent=2)

# Read from file
with open("data.json") as f:
    loaded = json.load(f)

# String conversion
s = json.dumps(data)         # dict → JSON string
d = json.loads(s)            # JSON string → dict
```

### `pathlib` — modern preferred API
```python
from pathlib import Path

p = Path("data") / "file.txt"
p.write_text("hello", encoding="utf-8")      # write
text = p.read_text(encoding="utf-8")         # read
p.exists(), p.is_file(), p.is_dir()
p.stat().st_size                             # file size in bytes
list(Path(".").glob("*.py"))                 # find all .py files
list(Path(".").rglob("*.txt"))              # recursive search
p.rename("new_name.txt")
p.unlink()                                   # delete file
```

---

## 🚀 Run It

```powershell
python file_io.py
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [fundamentals](../README.md)*
