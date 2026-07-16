# Skip and Selectively Run Tests in pytest

import sys
import pytest

# Simple functions to test
def calc_total(a, b):
    return a + b

def calc_multiply(a, b):
    return a * b

# 1. Skip a test unconditionally
@pytest.mark.skip(reason="This feature is not implemented yet")
def test_not_implemented():
    assert False

# 2. Skip a test conditionally (e.g., skip on Windows, or if Python version is too low)
@pytest.mark.skipif(sys.platform == "win32", reason="Does not run on Windows")
def test_mac_only():
    assert True

# 3. Custom markers to group and selectively run tests
@pytest.mark.windows
def test_windows_feature1():
    assert calc_total(2, 2) == 4

@pytest.mark.windows
def test_windows_feature2():
    assert calc_multiply(2, 3) == 6

@pytest.mark.mac
def test_mac_feature():
    assert True
