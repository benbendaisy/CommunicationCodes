from typing import List


class Solution:
    """
    Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

    Example 1:

    Input: arr = [1,2,2,6,6,6,6,7,10]
    Output: 6
    Example 2:

    Input: arr = [1,1]
    Output: 1
    """
    def findSpecialInteger1(self, arr: List[int]) -> int:
        num_counts = Counter(arr)
        target = len(arr) // 4
        for key, value in num_counts.items():
            if value > target:
                return key
        return -1
    
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        target = n // 4
        for i in range(n - target):
            if arr[i] == arr[i + target]:
                return arr[i]
        return -1