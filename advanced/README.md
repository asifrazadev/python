# 🔴 3 · Advanced Python

> **Videos 29–42** of the codebasics Complete Python 3 Tutorials
> **Prerequisites:** Complete [Intermediate](../intermediate/) (videos 19–28)

---

## 📋 Topics

| # | Video | Topic | File | Done |
|---|-------|-------|------|------|
| 29 | Multithreading Intro | `threading`, `Thread`, GIL | [`multithreading.py`](multithreading/multithreading.py) | ☐ |
| 30 | Multiprocessing Intro | `multiprocessing`, `Process` | [`multiprocessing_intro.py`](multiprocessing_intro/multiprocessing_intro.py) | ☐ |
| 31 | Sharing Data — Array & Value | `Value`, `Array` shared memory | [`shared_memory.py`](shared_memory/shared_memory.py) | ☐ |
| 32 | Sharing Data — Queue | `Queue` between processes | [`process_queue.py`](process_queue/process_queue.py) | ☐ |
| 33 | Multiprocessing Lock | `Lock`, race conditions | [`process_lock.py`](process_lock/process_lock.py) | ☐ |
| 34 | Pool — Map Reduce | `Pool.map()`, parallel tasks | [`pool_map.py`](pool_map/pool_map.py) | ☐ |
| 35 | pytest Introduction | `pytest`, test functions, assertions | [`test_intro.py`](pytest_intro/test_intro.py) | ☐ |
| 36 | pytest — skip & selective run | `@pytest.mark.skip`, `-k` filter | [`test_selective.py`](pytest_selective/test_selective.py) | ☐ |
| 37 | pytest fixtures | `@pytest.fixture`, setup/teardown | [`test_fixtures.py`](pytest_fixtures/test_fixtures.py) | ☐ |
| 38 | pytest parameters | `@pytest.mark.parametrize` | [`test_params.py`](pytest_params/test_params.py) | ☐ |
| 39 | numpy Intro | Arrays vs lists, `np.array` | [`numpy_intro.py`](numpy_intro/numpy_intro.py) | ☐ |
| 40 | numpy Basic Operations | Arithmetic, shape, dtype, reshape | [`numpy_ops.py`](numpy_ops/numpy_ops.py) | ☐ |
| 41 | numpy Slicing / Stacking | Slicing, `hstack`, `vstack`, boolean indexing | [`numpy_slicing.py`](numpy_slicing/numpy_slicing.py) | ☐ |
| 42 | numpy nditer | Iterating arrays with `np.nditer` | [`numpy_nditer.py`](numpy_nditer/numpy_nditer.py) | ☐ |

---

## 📦 Requirements

```powershell
pip install pytest numpy
```

---

## 🚀 Running Scripts

```powershell
python multithreading/multithreading.py

# Run tests
pytest pytest_intro/test_intro.py
```

---

*← [intermediate](../intermediate/) · [home →](../README.md)*
