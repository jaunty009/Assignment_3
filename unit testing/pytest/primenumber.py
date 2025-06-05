import pytest
import math

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

def test_not_prime():
    assert not is_prime_simple(0)   
    assert not is_prime_simple(1)    
    assert not is_prime_simple(4)   
  

def test_prime():
    assert is_prime_simple(2)   
    assert is_prime_simple(3)      
    assert is_prime_simple(5)       
 
