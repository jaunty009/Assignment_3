def is_even(n):
    return n % 2 == 0

import unittest

class TestIsEven(unittest.TestCase):
    def test_even(self):
        self.assertTrue(is_even(4))

    def test_odd(self):
        self.assertFalse(is_even(5))

    def test_zero(self):
        self.assertTrue(is_even(0))
        
if __name__ == '__main__':
     unittest.main()