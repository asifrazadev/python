# Command Line Argument Processing (argparse)

Part of the **Intermediate Python** series. → [Back to intermediate](../README.md)

---

## 📖 What's Covered

| Concept | Description |
|---------|-------------|
| **`argparse`** | Standard library module to write user-friendly command-line interfaces. |
| **Positional Arguments** | Required arguments parsed by position (e.g. `python cli_args.py 5 10`). |
| **Optional Arguments** | Prefixed with `-` or `--`, optional or have defaults (e.g. `--operation mul`). |
| **Automatic Help** | Built-in support for generating help screens using `-h` or `--help`. |

---

## 🧠 Key Concepts & Gotchas

### Positional vs Optional Arguments
- **Positional**: Required by default. Their order matches how they are added in code.
```python
parser.add_argument("num1", type=float) # positional
```
- **Optional**: Prefixed with `-` or `--`. Can specify a default fallback value.
```python
parser.add_argument("--operation", default="add") # optional
```

### Type Conversion
By default, command-line arguments are parsed as strings (`str`). Always define `type` parameter if you expect integers, floats, or booleans.
```python
parser.add_argument("num1", type=float)
```

---

## 🚀 Run It

```powershell
# Get help screen
python cli_args.py --help

# Basic usage (defaults to addition)
python cli_args.py 10 5

# Custom operation
python cli_args.py 10 5 --operation mul
```

---

## 📝 My Notes

<!-- Add your personal notes here -->

---

*← [intermediate](../README.md)*
