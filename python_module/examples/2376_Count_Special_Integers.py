class Solution:
    """
    We call a positive integer special if all of its digits are distinct.

    Given a positive integer n, return the number of special integers that belong to the interval [1, n].

    Example 1:

    Input: n = 20
    Output: 19
    Explanation: All the integers from 1 to 20, except 11, are special. Thus, there are 19 special integers.
    Example 2:

    Input: n = 5
    Output: 5
    Explanation: All the integers from 1 to 5 are special.
    Example 3:

    Input: n = 135
    Output: 110
    Explanation: There are 110 integers from 1 to 135 that are special.
    Some of the integers that are not special are: 22, 114, and 131.
    """
    def countSpecialNumbers1(self, n: int) -> int:
        """
        TLE
        """
        def check_special(m: int) -> bool:
            if m <= 10:
                return True
            mask = 0
            while m:
                r = m % 10
                if mask & (1 << r) != 0:
                    return False
                m = m // 10
                mask = mask | (1 << r)
            return True
        cnt = 0
        for i in range(1, n + 1):
            if check_special(i):
                cnt += 1
        return cnt
    
    def countSpecialNumbers2(self, n: int) -> int:
        digits = list(map(int, str(n)))  # Convert n to a list of digits
        length = len(digits)
        
        @lru_cache(None)
        def dp(pos: int, mask: int, is_tight: bool, is_started: bool) -> int:
            """
            pos: Current digit position.
            mask: Bitmask representing used digits.
            is_tight: Whether we are bound by the given number n.
            is_started: Whether we have placed a nonzero digit.
            """
            if pos == length:
                return 1 if is_started else 0  # Count valid numbers

            limit = digits[pos] if is_tight else 9  # Upper bound for this digit
            count = 0
            
            # If we haven't started, we can choose to skip this digit (leading zero case)
            if not is_started:
                count += dp(pos + 1, mask, False, False)  # Skip leading zeros
            
            # Try each digit 0-9
            for d in range(0 if is_started else 1, limit + 1):
                if mask & (1 << d) == 0:  # Ensure uniqueness
                    count += dp(
                        pos + 1, 
                        mask | (1 << d), 
                        is_tight and (d == limit), 
                        True
                    )

            return count

        return dp(0, 0, True, False)
    
    def countSpecialNumbers3(self, n: int) -> int:
        def is_special(m: int) -> bool:
            digits = list(map(int, str(m)))
            mask = 0
            for num in digits:
                if mask & (1 << num) != 0:
                    return False
                mask |= 1 << num
            return True
        
        cnt = 0
        for i in range(1, n + 1):
            if is_special(i):
                cnt += 1
        return cnt
    
    def countSpecialNumbers4(self, n: int) -> int:
        str_n = str(n)
        len_n = len(str_n)
        
        # Count numbers with fewer digits
        cnt = 0
        for i in range(1, len_n):
            f = 9
            for j in range(1, i):
                f *= (10 - j)  # Ensure digits remain unique
            cnt += f
        
        # Count numbers with same length as n using DFS
        @cache
        def helper(idx: int, is_prefix_limit: bool, used_mask: int) -> int:
            if idx == len_n:
                return 1  # Reached a valid number

            total = 0
            upper_bound = int(str_n[idx]) if is_prefix_limit else 9
            for digit in range(0 if idx > 0 else 1, upper_bound + 1):  # No leading zeros
                if (used_mask >> digit) & 1:  # Ensure uniqueness
                    continue
                total += helper(idx + 1, is_prefix_limit and digit == upper_bound, used_mask | (1 << digit))
            return total

        cnt += helper(0, True, 0)
        return cnt

    def countSpecialNumbers(self, n: int) -> int:
        str_n = str(n)
        len_n = len(str_n)

        cnt = 0
        for i in range(1, len_n):
            f = 9
            for j in range(1, i):
                f *= (10 - j)
            cnt += f
        
        @cache
        def helper(idx: int, is_prefix_limit: bool, mask: int) -> int:
            if idx == len_n:
                return 1
            
            total = 0
            upper_bound = int(str_n[idx]) if is_prefix_limit else 9
            for digit in range(0 if idx > 0 else 1, upper_bound + 1):
                if (mask & (1 << digit)) != 0:
                    continue
                
                total += helper(idx + 1, is_prefix_limit and digit == upper_bound, mask | (1 << digit))
            return total
        
        cnt += helper(0, True, 0)
        return cnt