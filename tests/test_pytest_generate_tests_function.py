import pytest

def subtract(a, b):
    return a - b

@pytest.fixture
def subtraction_function():
    return subtract

@pytest.mark.parametrize("subtraction_input", [
    (5, 2, 3),
    (10, 5, 5),
    (-8, 3, -11)
])
def test_subtraction(subtraction_function, subtraction_input):
    a, b, expected = subtraction_input
    result = subtraction_function(a, b)
    assert result == expected, f"Expected {expected}, but got {result}"
