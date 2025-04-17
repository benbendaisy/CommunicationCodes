class Solution:
    """
    Given a single-digit integer d and two integers low and high, return the number of times that d occurs as a digit in all integers in the inclusive range [low, high].

    Example 1:

    Input: d = 1, low = 1, high = 13
    Output: 6
    Explanation: The digit d = 1 occurs 6 times in 1, 10, 11, 12, 13.
    Note that the digit d = 1 occurs twice in the number 11.
    Example 2:

    Input: d = 3, low = 100, high = 250
    Output: 35
    Explanation: The digit d = 3 occurs 35 times in 103,113,123,130,131,...,238,239,243.
    """
    def digitsCount1(self, d: int, low: int, high: int) -> int:
        cnt = 0
        for i in range(low, high + 1):
            cnt += str(i).count(str(d))
        return cnt
    
    def digitsCount2(self, d: int, low: int, high: int) -> int:
        def count_occurrence(n: int) -> int:
            if n < 0:
                return 0
            
            digits = list(map(int, str(n)))
            length = len(digits)

            @cache
            def helper(idx: int, is_prefix_limit: bool, cnt: int, leading_zero: bool) -> int:
                if idx == length:
                    return cnt  # Base case: return count of d
                
                total = 0
                upper = digits[idx] if is_prefix_limit else 9
                
                for digit in range(upper + 1):
                    new_cnt = cnt
                    if digit == d and (d != 0 or not leading_zero):
                        new_cnt += 1  # Count non-leading zeros

                    total += helper(
                        idx + 1,
                        is_prefix_limit and (digit == upper),
                        new_cnt,
                        leading_zero and digit == 0  # Continue tracking leading zeros
                    )
                
                return total

            return helper(0, True, 0, True)  # Start with leading_zero=True

        return count_occurrence(high) - count_occurrence(low - 1)
    
    def digitsCount3(self, d: int, low: int, high: int) -> int:
        def count_occurrence(n: int) -> int:
            if n < 0:
                return 0
            digits = list(map(int, str(n)))
            length = len(digits)

            @cache
            def helper(idx: int, is_prefix_limit: bool, cnt: int, leading_zero: bool) -> int:
                if idx == length:
                    return cnt
                
                total = 0
                upper = digits[idx] if is_prefix_limit else 9
                for digit in range(upper + 1):
                    new_cnt = cnt
                    if digit == d and (d != 0 or not leading_zero):
                        new_cnt += 1
                    total += helper(idx + 1, is_prefix_limit and (digit == upper), new_cnt, leading_zero and digit == 0)
                return total
            return helper(0, True, 0, True)
        return count_occurrence(high) - count_occurrence(low - 1)
    
    def digitsCount4(self, d: int, low: int, high: int) -> int:
        def count_occurence(num):
            if num < 0:
                return 0
            digits = list(map(int, str(num)))
            length = len(digits)

            @cache
            def helper(idx: int, is_prefix_limit: bool, cnt: int, leading_zero: bool) -> int:
                if idx == length:
                    return cnt
                
                total = 0
                upper = digits[idx] if is_prefix_limit else 9
                for digit in range(upper + 1):
                    new_cnt = cnt
                    if digit == d and (d != 0 or not leading_zero):
                        new_cnt += 1
                    total += helper(idx + 1, (digit == upper) and is_prefix_limit, new_cnt, leading_zero and digit == 0)
                return total
            return helper(0, True, 0, True)
        return count_occurence(high) - count_occurence(low - 1)