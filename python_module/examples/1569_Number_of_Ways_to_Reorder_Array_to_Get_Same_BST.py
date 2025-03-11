from typing import List
from math import comb

class Solution:
    """
    Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

    For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
    Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

    Since the answer may be very large, return it modulo 109 + 7.

    Example 1:

    Input: nums = [2,1,3]
    Output: 1
    Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.
    Example 2:

    Input: nums = [3,4,5,1,2]
    Output: 5
    Explanation: The following 5 arrays will yield the same BST: 
    [3,1,2,4,5]
    [3,1,4,2,5]
    [3,1,4,5,2]
    [3,4,1,2,5]
    [3,4,1,5,2]
    Example 3:

    Input: nums = [1,2,3]
    Output: 0
    Explanation: There are no other orderings of nums that will yield the same BST.
    """
    def numOfWays1(self, nums: List[int]) -> int:
        mod = (10**9) + 7
        
        def func(arr):
            if len(arr) <= 2:
                return 1
            left = [v for v in arr if v < arr[0]]
            right = [v for v in arr if v > arr[0]]
            return comb(len(left) + len(right), len(right)) * func(left) * func(right)
        
        return (func(nums) - 1) % mod
    
    def numOfWays2(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        # Recursive function to count ways to form the same BST
        @lru_cache(None)
        def countWays(arr):
            if len(arr) <= 2:
                return 1  # Base case: Only 1 way to arrange a list of ≤2 elements
            
            root = arr[0]
            left_subtree = [x for x in arr if x < root]
            right_subtree = [x for x in arr if x > root]
            
            # Compute number of ways recursively
            left_ways = countWays(tuple(left_subtree))
            right_ways = countWays(tuple(right_subtree))

            # Compute the number of ways to merge left and right while keeping order
            interleave_ways = comb(len(left_subtree) + len(right_subtree), len(left_subtree))

            return (left_ways * right_ways * interleave_ways) % mod

        return (countWays(tuple(nums)) - 1) % mod  # Exclude original ordering
    
    def numOfWays(self, nums: List[int]) -> int:
        mod = 10 ** 9 + 7
        @cache
        def helper(arr: tuple) -> int:
            if len(arr) <= 2:
                return 1
            
            left_sub = [x for x in arr if x < arr[0]]
            right_sub = [x for x in arr if x > arr[0]]

            left_ways = helper(tuple(left_sub))
            right_ways = helper(tuple(right_sub))

            inter_ways = comb(len(left_sub) + len(right_sub), len(left_sub))
            return (left_ways * right_ways * inter_ways) % mod
        
        return (helper(tuple(nums)) - 1)