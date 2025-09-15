def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def divide(a, b):
    if b == 0:
        raise ValueError("not divisible by zero")
    return a / b


import unittest

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 4), 5)

    def test_multiply(self):
        self.assertEqual(multiply(2, 5), 10)
        
    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_divide(self):
        self.assertEqual(divide(8, 2), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(0, 5)

if __name__ == '__main__':
    unittest.main()