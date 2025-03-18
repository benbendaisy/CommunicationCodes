class Solution:
    """
    You are given two numeric strings num1 and num2 and two integers max_sum and min_sum. We denote an integer x to be good if:

    num1 <= x <= num2
    min_sum <= digit_sum(x) <= max_sum.
    Return the number of good integers. Since the answer may be large, return it modulo 109 + 7.

    Note that digit_sum(x) denotes the sum of the digits of x.

    Example 1:

    Input: num1 = "1", num2 = "12", min_sum = 1, max_sum = 8
    Output: 11
    Explanation: There are 11 integers whose sum of digits lies between 1 and 8 are 1,2,3,4,5,6,7,8,10,11, and 12. Thus, we return 11.
    Example 2:

    Input: num1 = "1", num2 = "5", min_sum = 1, max_sum = 5
    Output: 5
    Explanation: The 5 integers whose sum of digits lies between 1 and 5 are 1,2,3,4, and 5. Thus, we return 5.
    """
    def count1(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        """
        TIME LIMIT EXCEEDED
        """
        num1, num2 = int(num1), int(num2)
        mod = 10 ** 9 + 7
        def digit_sum(x: int):
            return sum(map(int, str(x)))
        
        cnt = 0
        for i in range(num1, num2 + 1):
            if min_sum <= digit_sum(i) <= max_sum:
                cnt += 1
        return cnt % mod
    
    def count2(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        mod = 10**9 + 7
        
        def count_valid_numbers(n: str) -> int:
            """Returns the count of numbers ≤ n with digit sum in range [min_sum, max_sum]"""
            @lru_cache(None)
            def dp(pos: int, tight: bool, digit_sum: int) -> int:
                if digit_sum > max_sum:  # Prune if sum exceeds max_sum
                    return 0
                if pos == len(n):  # Base case: Check if sum is within range
                    return min_sum <= digit_sum <= max_sum
                
                limit = int(n[pos]) if tight else 9
                res = 0
                for digit in range(0, limit + 1):  # Try all possible digits
                    res += dp(pos + 1, tight and (digit == limit), digit_sum + digit)
                return res
            
            return dp(0, True, 0)  # Start recursion from first digit

        num1, num2 = int(num1), int(num2)
        return (count_valid_numbers(str(num2)) - count_valid_numbers(str(num1 - 1))) % mod
    
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        mod = 10 ** 9 + 7

        def count_valid_numbers(n: str) -> int:
            @cache
            def helper(idx: int, is_prefix_limit: bool, digit_sum: int) -> int:
                if digit_sum > max_sum:
                    return 0
                
                if idx == len(n):
                    return min_sum <= digit_sum <= max_sum
                upper = int(n[idx]) if is_prefix_limit else 9
                cnt = 0
                for digit in range(0, upper + 1):
                    cnt += helper(idx + 1, is_prefix_limit and (digit == upper), digit_sum + digit)
                return cnt
            return helper(0, True, 0)
        num1 = int(num1)
        return (count_valid_numbers(num2) - count_valid_numbers(str(num1 - 1))) % mod