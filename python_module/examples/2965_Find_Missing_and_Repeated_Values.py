class Solution:
    """
    You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

    Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

    Example 1:

    Input: grid = [[1,3],[2,2]]
    Output: [2,4]
    Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].
    Example 2:

    Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
    Output: [9,5]
    Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].
    """
    def findMissingAndRepeatedValues1(self, grid: List[List[int]]) -> List[int]:
        if not grid:
            return 0
        
        n = len(grid)
        arr = [0] * (n ** 2)

        for i in range(n):
            for j in range(n):
                v = grid[i][j]
                arr[v - 1] += 1
        res = [0] * 2
        for i in range(n ** 2):
            if arr[i] == 0:
                res[1] = i + 1
            
            if arr[i] == 2:
                res[0] = i + 1
        return res
    
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        if not grid:
            return 0
        n = len(grid)
        expected_sums = sum(range(n ** 2 + 1))
        expected_square_sums = sum(i ** 2 for i in range(n ** 2 + 1))

        real_sums, real_square_sums = 0, 0
        for i in range(n):
            for j in range(n):
                real_sums += grid[i][j]
                real_square_sums += grid[i][j] ** 2
        
        #  x - y
        diff1 = expected_sums - real_sums
        diff2 = expected_square_sums - real_square_sums
        # x + y
        sum_xy = diff2 / diff1
        x = (diff1 + sum_xy) // 2
        y = sum_xy - x
        return [int(y), int(x)]