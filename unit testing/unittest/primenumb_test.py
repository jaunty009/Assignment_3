import math
import unittest

def is_prime_simple(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

class TestIsPrimeSimple(unittest.TestCase):
    def test_not_prime(self): 
        self.assertFalse(is_prime_simple(0))    # 0 is not prime
        self.assertFalse(is_prime_simple(1))    # 1 is not prime
        self.assertFalse(is_prime_simple(4))    # 4 is divisible by 2
        
    def test_prime(self):
        self.assertTrue(is_prime_simple(2))     # 2 is prime
        self.assertTrue(is_prime_simple(3))     # 3 is prime
        self.assertTrue(is_prime_simple(5))     # 5 is prime

if __name__ == '__main__':
    unittest.main()