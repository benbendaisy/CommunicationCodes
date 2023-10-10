class Solution:
    """
    You are given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:

    You should build the array arr which has the following properties:

    arr has exactly n integers.
    1 <= arr[i] <= m where (0 <= i < n).
    After applying the mentioned algorithm to arr, the value search_cost is equal to k.
    Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.
    
    Example 1:

    Input: n = 2, m = 3, k = 1
    Output: 6
    Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
    Example 2:

    Input: n = 5, m = 2, k = 3
    Output: 0
    Explanation: There are no possible arrays that satisify the mentioned conditions.
    Example 3:

    Input: n = 9, m = 1, k = 1
    Output: 1
    Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]
    """
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        mod = 10 ** 9 + 7
        @lru_cache(None)
        def helper(idx, max_so_far, remain):
            if idx == n:
                if remain == 0:
                    return 1
                return 0
            # We place a number that is not a new maximum. How many ways are there to do this? 
            # The range of numbers we could choose from is [1, max_so_far]
            number_ways = (max_so_far * helper(idx + 1, max_so_far, remain)) % mod
            for num in range(max_so_far + 1, m + 1):
                # We place a number that is a new maximum
                number_ways = (number_ways + helper(idx + 1, num, remain - 1)) % mod
                    
            return number_ways
        return helper(0, 0, k)