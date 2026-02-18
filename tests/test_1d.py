"""
tests_1d.py

This module contains unit tests for the two_sum function defined in lab_1d.py.
"""

import pytest
from labs.lab_1.lab_1d import two_sum

def test_standard_cases():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]    # Standard sequential
    assert two_sum([3, 2, 4], 6) == [1, 2]         # Out of order

def test_duplicate_numbers():
    assert two_sum([3, 3], 6) == [0, 1]            # Two identical numbers
    assert two_sum([5, 5, 5], 10) == [0, 1]        # More than two identical numbers (should pick first two)

def test_no_solution():
    assert two_sum([1, 2, 3, 4], 100) == []        # Valid input, but no pairs match

def test_negatives_and_zeroes():
    assert two_sum([-1, -2, -3, -4, -5], -8) == [2, 4] # Negative numbers
    assert two_sum([0, 4, 3, 0], 0) == [0, 3]          # Zeroes adding to zero
    assert two_sum([-10, 10, 5], 0) == [0, 1]          # Negative and positive adding to zero

def test_large_numbers():
    assert two_sum([1000000000, 5, 2000000000], 3000000000) == [0, 2] # Very large integers

def test_invalid_length():
    with pytest.raises(ValueError, match="List must contain at least two numbers"):
        two_sum([5], 5)                            # Only one element
    with pytest.raises(ValueError, match="List must contain at least two numbers"):
        two_sum([], 9)                             # Empty list

def test_invalid_type_nums_container():
    with pytest.raises(TypeError, match="Input 'nums' must be a list"):
        two_sum("not a list", 9)                   # String instead of list
    with pytest.raises(TypeError, match="Input 'nums' must be a list"):
        two_sum(None, 9)                           # NoneType

def test_invalid_type_target():
    with pytest.raises(TypeError, match="Input 'target' must be an integer"):
        two_sum([2, 7], "9")                       # String target
    with pytest.raises(TypeError, match="Input 'target' must be an integer"):
        two_sum([2, 7], 9.5)                       # Float target

def test_invalid_elements_inside_nums():
    with pytest.raises(ValueError, match="All elements in the array must be integers"):
        two_sum([2, "7", 11], 9)                   # String inside the list
    with pytest.raises(ValueError, match="All elements in the array must be integers"):
        two_sum([2, 7.5, 11], 9)                   # Float inside the list
    with pytest.raises(ValueError, match="All elements in the array must be integers"):
        two_sum([2, None, 11], 9)                  # None inside the list

def test_boolean_trap():
    # Ensuring True/False aren't sneakily evaluated as 1 and 0
    with pytest.raises(ValueError, match="All elements in the array must be integers"):
        two_sum([True, False, 5], 1)               # Booleans in the list
    with pytest.raises(TypeError, match="Input 'target' must be an integer"):
        two_sum([2, 7], True)                      # Boolean as the target

if __name__ == "__main__":
    pytest.main()