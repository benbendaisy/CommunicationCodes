class Solution:
    """
    Given a positive integer n, find the pivot integer x such that:

    The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
    Return the pivot integer x. If no such integer exists, return -1. It is guaranteed that there will be at most one pivot index for the given input.

    Example 1:

    Input: n = 8
    Output: 6
    Explanation: 6 is the pivot integer since: 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21.
    Example 2:

    Input: n = 1
    Output: 1
    Explanation: 1 is the pivot integer since: 1 = 1.
    Example 3:

    Input: n = 4
    Output: -1
    Explanation: It can be proved that no such integer exist.
    """
    def pivotInteger1(self, n: int) -> int:
        for i in range(1, n + 1):
            left_sum = sum(range(1, i + 1))
            right_sum = sum(range(i, n + 1))
            if left_sum == right_sum:
                return i
        return -1

    def pivotInteger(self, n: int) -> int:
        left, right = 1, n
        total_sum = n * (n + 1) // 2
        while left < right:
            mid = (left + right) // 2
            if mid * mid - total_sum < 0:
                left = mid + 1
            else:
                right = mid
        if left * left - total_sum == 0:
            return left
        return -1
    
    def waysToReachTarget(self, target: int, types: List[List[int]]) -> int:
        if not types:
            return 0

        mod = 10 ** 9 + 7
        @cache
        def helper(idx: int, running_sum: int) -> int:
            if running_sum == target:
                return 1
            
            if idx == len(types):
                return 0
            
            ways = 0
            for i in range(idx, len(types)):
                cnt, mark = types[i]
                for j in range(cnt):
                    new_sum = running_sum + (j + 1) * mark
                    if new_sum <= target:
                        ways += helper(i + 1, new_sum)
            return ways % mod
        
        return helper(0, 0)
