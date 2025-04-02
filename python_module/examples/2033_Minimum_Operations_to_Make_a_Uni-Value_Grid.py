class Solution:
    """
    You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

    A uni-value grid is a grid where all the elements of it are equal.

    Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

    Example 1:

    Input: grid = [[2,4],[6,8]], x = 2
    Output: 4
    Explanation: We can make every element equal to 4 by doing the following: 
    - Add x to 2 once.
    - Subtract x from 6 once.
    - Subtract x from 8 twice.
    A total of 4 operations were used.
    Example 2:

    Input: grid = [[1,5],[2,3]], x = 1
    Output: 5
    Explanation: We can make every element equal to 3.
    Example 3:

    Input: grid = [[1,2],[3,4]], x = 2
    Output: -1
    Explanation: It is impossible to make every element equal.
    """
    def minOperations1(self, grid: List[List[int]], x: int) -> int:
         # Flatten the grid to a 1D list
        nums = [num for row in grid for num in row]
        
        # Check if it's possible to make the grid uni-value
        remainder = nums[0] % x
        for num in nums:
            if num % x != remainder:
                return -1
        
        # Sort the numbers to find the median efficiently
        nums.sort()
        median = nums[len(nums) // 2]
        
        # Compute the number of operations needed to make all elements equal to the median
        operations = sum(abs(num - median) // x for num in nums)
        
        return operations
    
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        if not grid:
            return -1
        m, n = len(grid), len(grid[0])
        nums = [grid[r][c] for r in range(m) for c in range(n)]
        remainder = nums[0] % x
        if(any(num % x != remainder for num in nums)):
            return -1
        nums.sort()
        median = nums[len(nums) // 2]
        ops = sum(abs(num - median) // x for num in nums)
        return ops