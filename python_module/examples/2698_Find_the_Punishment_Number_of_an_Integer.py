class Solution:
    """
    Given a positive integer n, return the punishment number of n.

    The punishment number of n is defined as the sum of the squares of all integers i such that:

    1 <= i <= n
    The decimal representation of i * i can be partitioned into contiguous substrings such that the sum of the integer values of these substrings equals i.
    
    Example 1:

    Input: n = 10
    Output: 182
    Explanation: There are exactly 3 integers i in the range [1, 10] that satisfy the conditions in the statement:
    - 1 since 1 * 1 = 1
    - 9 since 9 * 9 = 81 and 81 can be partitioned into 8 and 1 with a sum equal to 8 + 1 == 9.
    - 10 since 10 * 10 = 100 and 100 can be partitioned into 10 and 0 with a sum equal to 10 + 0 == 10.
    Hence, the punishment number of 10 is 1 + 81 + 100 = 182
    Example 2:

    Input: n = 37
    Output: 1478
    Explanation: There are exactly 4 integers i in the range [1, 37] that satisfy the conditions in the statement:
    - 1 since 1 * 1 = 1. 
    - 9 since 9 * 9 = 81 and 81 can be partitioned into 8 + 1. 
    - 10 since 10 * 10 = 100 and 100 can be partitioned into 10 + 0. 
    - 36 since 36 * 36 = 1296 and 1296 can be partitioned into 1 + 29 + 6.
    Hence, the punishment number of 37 is 1 + 81 + 100 + 1296 = 1478
    """
    def punishmentNumber1(self, n: int) -> int:
        def partition(x, target):
            if x == target: return True
            if x == 0: return target == 0
            for m in (10, 100, 1000):
                if partition(x//m, target - x % m):
                    return True
            return False
        return sum([x**2 for x in range(1, n + 1) if partition(x * x, x)])
    
    def punishmentNumber(self, n: int) -> int:
        def partition(string_num, target):
            if not string_num and target == 0:
                return True
            if not string_num or target < 0:
                return False
            for idx in range(len(string_num)):
                left = string_num[:idx + 1]
                right = string_num[idx + 1:]
                left_num = int(left)
                if partition(right, target - left_num):
                    return True
            return False
        return sum([x**2 for x in range(1, n + 1) if partition(str(x * x), x)])