# pytest Parameterization Demonstration

import pytest

# Function to test
def calc_total(a, b):
    return a + b

# Parametrize test runs
# Arguments: (string of argument names, list of tuple values)
@pytest.mark.parametrize(
    "num1, num2, expected",
    [
        (3, 5, 8),      # test case 1
        (-1, 1, 0),     # test case 2
        (0, 0, 0),      # test case 3
        (10, 20, 30),   # test case 4
    ]
)
def test_calc_total(num1, num2, expected):
    assert calc_total(num1, num2) == expected
