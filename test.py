# square number

# import unittest

# def square(number):
#     """Return the square of a number."""
#     if not isinstance(number, (int, float)):
#         raise TypeError("Input must be a number")
#     return number ** 2

# class TestSquareFunction(unittest.TestCase):
#     def test_square_positive_integer(self):
#         self.assertEqual(square(5), 25)
    

# if __name__ == '__main__':
#     unittest.main()


# count vowels

# import unittest

# def count_vowels(text):
#     """Count vowels in a string (case-insensitive)."""
#     if not isinstance(text, str):
#         raise TypeError("Input must be a string")
#     return sum(1 for char in text.lower() if char in "aeiou")

# class TestVowelCount(unittest.TestCase):
#     def test_empty_string(self):
#         self.assertEqual(count_vowels(""), 0)
    
#     def test_no_vowels(self):
#         self.assertEqual(count_vowels("xyz"), 0)
    
#     def test_all_vowels(self):
#         self.assertEqual(count_vowels("aeiou"), 5)
    
#     def test_non_string_input(self):
#         with self.assertRaises(TypeError):
#             count_vowels(123)

# if __name__ == '__main__':
#     unittest.main()

# max number in a list

# import unittest

# def find_max(numbers):
#     """
#     Return the maximum number in a list.
    
#     Args:
#         numbers: List of numbers (ints or floats)
        
#     Returns:
#         The maximum number in the list
        
#     Raises:
#         TypeError: If input is not a list
#         ValueError: If list is empty or contains non-numbers
#     """
#     if not isinstance(numbers, list):
#         raise TypeError("Input must be a list")
#     if not numbers:
#         raise ValueError("List cannot be empty")
#     if not all(isinstance(x, (int, float)) for x in numbers):
#         raise ValueError("All elements must be numbers")
    
#     max_num = numbers[0]
#     for num in numbers[1:]:
#         if num > max_num:
#             max_num = num
#     return max_num

# class TestFindMax(unittest.TestCase):
#     def test_positive_numbers(self):
#         self.assertEqual(find_max([1, 2, 3, 4]), 4)
    
#     def test_negative_numbers(self):
#         self.assertEqual(find_max([-1, -2, -3, -4]), -1)

# if __name__ == '__main__':
#     unittest.main()

# reverse a string

# import unittest

# def reverse_list(lst):
#     """
#     Reverse the elements of a list.
    
#     Args:
#         lst: List to be reversed (can contain any elements)
        
#     Returns:
#         New list with elements in reverse order
        
#     Raises:
#         TypeError: If input is not a list
#     """
#     if not isinstance(lst, list):
#         raise TypeError("Input must be a list")
#     return lst[::-1]

# class TestReverseList(unittest.TestCase):
#     def test_normal_list(self):
#         self.assertEqual(reverse_list([1, 2, 3, 4]), [4, 3, 2, 1])
    
# if __name__ == '__main__':
#     unittest.main()


# prime numbers

# import unittest
# import math

# def is_prime(n):
#     """
#     Check if a number is prime.
    
#     Args:
#         n: Integer to check
        
#     Returns:
#         True if n is prime, False otherwise
        
#     Raises:
#         TypeError: If input is not an integer
#         ValueError: If input is less than 2
#     """
#     if not isinstance(n, int):
#         raise TypeError("Input must be an integer")
#     if n < 2:
#         raise ValueError("Number must be greater than 1")
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
    
#     sqrt_n = math.isqrt(n) + 1
#     for i in range(3, sqrt_n, 2):
#         if n % i == 0:
#             return False
#     return True

# class TestIsPrime(unittest.TestCase):
#     def test_small_primes(self):
#         primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
#         for p in primes:
#             self.assertTrue(is_prime(p), f"{p} should be prime")
    
#     def test_small_non_primes(self):
#         non_primes = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
#         for np in non_primes:
#             self.assertFalse(is_prime(np), f"{np} should not be prime")

# if __name__ == '__main__':
#     unittest.main()

# factorial

# import unittest
# import math

# def factorial(n):
#     """
#     Calculate the factorial of a non-negative integer.
    
#     Args:
#         n: Non-negative integer
        
#     Returns:
#         Factorial of n (n!)
        
#     Raises:
#         TypeError: If input is not an integer
#         ValueError: If input is negative
#     """
#     if not isinstance(n, int):
#         raise TypeError("Input must be an integer")
#     if n < 0:
#         raise ValueError("Factorial is not defined for negative numbers")
#     if n == 0:
#         return 1
#     return n * factorial(n - 1)

# class TestFactorial(unittest.TestCase):
#     def test_base_case(self):
#         self.assertEqual(factorial(0), 1)
    
#     def test_small_numbers(self):
#         self.assertEqual(factorial(1), 1)
#         self.assertEqual(factorial(2), 2)
#         self.assertEqual(factorial(3), 6)
#         self.assertEqual(factorial(4), 24)
#         self.assertEqual(factorial(5), 120)

# if __name__ == '__main__':
#     unittest.main()
    
    
    # addition
    
# import unittest

# class Calculator:
#     """A simple calculator class with basic arithmetic operations"""
    
#     def add(self, a, b):
#         """Return the sum of two numbers"""
#         if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#             raise TypeError("Both arguments must be numbers")
#         return a + b

# class TestCalculator(unittest.TestCase):
#     """Unit tests for the Calculator class"""
    
#     def setUp(self):
#         """Create a Calculator instance before each test"""
#         self.calc = Calculator()
        
#     def test_add_integers(self):
#         self.assertEqual(self.calc.add(2, 3), 5)
    
#     def test_add_floats(self):
#         self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)
            
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
    
    
    # subtraction
# import unittest

# class Calculator:
#     """A simple calculator class with subtraction operation"""
    
#     def subtract(self, a, b):
#         """Return the difference between two numbers (a - b)"""
#         if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#             raise TypeError("Both arguments must be numbers")
#         return a - b

# class TestCalculator(unittest.TestCase):
#     """Unit tests for the Calculator's subtraction method"""
    
#     def setUp(self):
#         """Create a Calculator instance before each test"""
#         self.calc = Calculator()
    
#     def test_subtract_positive_integers(self):
#         """Test subtracting smaller positive integer from larger one"""
#         self.assertEqual(self.calc.subtract(5, 3), 2)
    
#     def test_subtract_negative_result(self):
#         """Test subtraction that yields negative result"""
#         self.assertEqual(self.calc.subtract(3, 5), -2)
    
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
 
# multiplication

# import unittest

# class Calculator:
#     """A simple calculator class with multiplication operation"""
    
#     def multiply(self, a, b):
#         """Return the product of two numbers"""
#         if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#             raise TypeError("Both arguments must be numbers")
#         return a * b

# class TestCalculator(unittest.TestCase):
#     """Unit tests for the Calculator's multiplication method"""
    
#     def setUp(self):
#         """Create a Calculator instance before each test"""
#         self.calc = Calculator()
    
#     def test_multiply_positive_integers(self):
#         """Test multiplying positive integers"""
#         self.assertEqual(self.calc.multiply(3, 4), 12)
    
#     def test_multiply_negative_numbers(self):
#         """Test multiplying negative numbers"""
#         self.assertEqual(self.calc.multiply(-3, -4), 12)
    
   
# if __name__ == '__main__':
#     unittest.main(verbosity=2)

# division

# import unittest

# class Calculator:
#     """A simple calculator class with division operation"""
    
#     def divide(self, a, b):
#         """Return the quotient of two numbers (a / b)"""
#         if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
#             raise TypeError("Both arguments must be numbers")
#         if b == 0:
#             raise ValueError("Cannot divide by zero")
#         return a / b

# class TestCalculator(unittest.TestCase):
#     """Unit tests for the Calculator's division method"""
    
#     def setUp(self):
#         """Create a Calculator instance before each test"""
#         self.calc = Calculator()
    
#     def test_divide_integers_exact(self):
#         """Test exact integer division"""
#         self.assertEqual(self.calc.divide(6, 3), 2)
    
#     def test_divide_integers_float_result(self):
#         """Test integer division that results in float"""
#         self.assertEqual(self.calc.divide(5, 2), 2.5)
        
# if __name__ == '__main__':
#     unittest.main(verbosity=2)
