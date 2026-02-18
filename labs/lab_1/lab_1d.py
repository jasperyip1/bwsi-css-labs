"""
lab_1d.py

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Derived from LeetCode problem: https://leetcode.com/problems/two-sum/ (leetcode easy)
"""

# TODO: Find and resolve the bug in the following implementation. Create unit tests to verify your fix.
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    Function that takes in a list of integers and a target integer, and returns the indices of the two numbers that add up to the target.

    Args:
        nums (list[int]): List of integers.
        target (int): Target integer.
    
    Returns:
        list[int]: Indices of the two numbers that add up to the target.
    """

    if not isinstance(nums, list):
        raise TypeError("Input 'nums' must be a list.")
    if not isinstance(target, int) or isinstance(target, bool):
        raise TypeError("Input 'target' must be an integer.") # Check if 'nums' is a list and 'target' is an integer

    if len(nums) < 2:
        raise ValueError("List must contain at least two numbers.") # Check if the list has at least two elements

    if not all(isinstance(x, int) and not isinstance(x, bool) for x in nums):
        raise ValueError("All elements in the array must be integers.") # Check if all elements in the list are integers
    
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    return []  # In case there is no solution, though the problem guarantees one exists.

# Example usage:
def main():
    nums = [2, 7, 11, 15]
    target = 9
    result = two_sum(nums, target)
    print(f"Indices of the two numbers that add up to {target}: {result}")

if __name__ == "__main__":
    main()