import pytest

def max_value(lst):
    if not lst:
        return None
    max_val = lst[0]
    for num in lst[1:]:
        if num > max_val:
            max_val = num
    return max_val

def test_positive_numbers():
        assert max_value([1, 2, 3, 4, 5]) == 5 
    
def test_negative_numbers():
        assert max_value([-1, -2, -3, -4, -5]) == -1
    
def test_empty_list():
        assert max_value([]) == None
    

