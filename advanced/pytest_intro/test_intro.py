# Simple pytest demonstration

# Function to test
def calc_total(a, b):
    return a + b

def calc_multiply(a, b):
    return a * b

# Test cases (pytest will look for functions prefixed with "test_")
def test_calc_total():
    total = calc_total(4, 5)
    assert total == 9, "4 + 5 should be 9"

def test_calc_multiply():
    result = calc_multiply(10, 3)
    assert result == 30, "10 * 3 should be 30"
