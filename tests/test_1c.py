"""
tests_1c.py

This module contains unit tests for the max_subarray_sum function defined in lab_1c.py.
"""

import pytest
from labs.lab_1.lab_1c import max_subarray_sum

def test_standard_cases():
    assert max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6  # Classic mixed array
    assert max_subarray_sum([1, 2, 3, 4, 5]) == 15                 # All positive numbers
    assert max_subarray_sum([-2, 10, 20, 30, -5]) == 60            # Max subarray isolated in the middle

def test_single_elements():
    assert max_subarray_sum([7]) == 7                              # Single positive element
    assert max_subarray_sum([-3]) == -3                            # Single negative element
    assert max_subarray_sum([0]) == 0                              # Single zero

def test_all_negative_elements():
    # Note: Assumes the algorithm is required to pick at least one element
    assert max_subarray_sum([-5, -2, -9, -1, -4]) == -1            # Must pick the smallest negative
    assert max_subarray_sum([-10, -10, -10]) == -10                # Identical negative numbers

def test_zeroes_and_mixed_cases():
    assert max_subarray_sum([0, 0, 0, 0]) == 0                     # All zeroes
    assert max_subarray_sum([0, -3, 1, 0, 2, -1, 0, 4, 0, -2]) == 6 # Zeroes mixed with positives/negatives

def test_boundary_max_positions():
    assert max_subarray_sum([15, -2, -5, 3, -8]) == 15             # Max subarray is just the very first element
    assert max_subarray_sum([-5, -2, 3, -8, 20]) == 20             # Max subarray is just the very last element
    assert max_subarray_sum([10, -5, 10, -20, 5]) == 15            # Max at beginning, ending right before a deep drop

def test_tricky_sequences():
    assert max_subarray_sum([50, -49, 50]) == 51                   # Bridging a negative gap (sides outweigh the middle)
    assert max_subarray_sum([50, -51, 50]) == 50                   # Not bridging a negative gap (drop is too steep)
    assert max_subarray_sum([100, -101, 100, -101, 100]) == 100    # Alternating large numbers, should not accumulate
    assert max_subarray_sum([1, -1, 1, -1, 1, -1, 1]) == 1         # Small alternating sequence

def test_empty_array():
    # Depending on your implementation, an empty array might return 0 or raise an error.
    # This assumes you wrote it to raise a ValueError.
    with pytest.raises(ValueError, match="Array must not be empty."):
        max_subarray_sum([])

def test_invalid_input_types():
    # Testing how the algorithm handles totally invalid data types
    with pytest.raises(TypeError):
        max_subarray_sum(None)
    with pytest.raises(TypeError):
        max_subarray_sum("not an array")

if __name__ == "__main__":
    pytest.main()