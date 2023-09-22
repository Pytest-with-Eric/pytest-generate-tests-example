# conftest.py
import pytest

def subtract(a, b):
    return a - b
    
@pytest.fixture(scope="module")
def subtraction_function():
    return subtract

def pytest_generate_tests(metafunc):
    if "subtraction_input" in metafunc.fixturenames:
        test_cases = [
            (5, 2, 3),
            (10, 5, 5),
            (-8, 3, -11)
        ]
        metafunc.parametrize("subtraction_input", test_cases)
