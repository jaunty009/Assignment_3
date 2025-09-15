def max_value(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_val = num
    return max_val


import unittest

class TestMaxValue(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_value([1, 2, 3, 4, 5]), 5)
    
    def test_negative_numbers(self):
        self.assertEqual(max_value([-1, -2, -3, -4, -5]), -1)
    
    def test_empty_list(self):
        self.assertIsNone(max_value([]))
    

if __name__ == '__main__':
    unittest.main()