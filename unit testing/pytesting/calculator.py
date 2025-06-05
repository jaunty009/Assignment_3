# test_calculator.py

# Simple function to test
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Tests using pytest
def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(3, 3) == 0
    assert subtract(0, 4) == -4