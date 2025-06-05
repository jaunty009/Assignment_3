import pytest

def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


    def test_no_duplicates():
        assert remove_duplicates([1, 2, 3]) == [1, 2, 3]
    
    def test_all_duplicates():
        assert remove_duplicates([4, 4, 4]) == [4]
    
    def test_mixed_duplicates():
        assert remove_duplicates([1, 2, 2, 3, 3, 3, 4]) == [1, 2, 3, 4]
    
    def test_empty_list():
        assert remove_duplicates([]) == []
