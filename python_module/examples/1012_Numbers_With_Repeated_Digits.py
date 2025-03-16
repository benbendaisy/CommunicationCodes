class Solution:
    """
    Given an integer n, return the number of positive integers in the range [1, n] that have at least one repeated digit.

    Example 1:

    Input: n = 20
    Output: 1
    Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
    Example 2:

    Input: n = 100
    Output: 10
    Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
    Example 3:

    Input: n = 1000
    Output: 262
    """
    def numDupDigitsAtMostN1(self, n: int) -> int:
        """
        TLE
        """
        def is_special(m: int) -> bool:
            digits = list(map(int, str(m)))
            mask = 0
            for num in digits:
                if mask & (1 << num) != 0:
                    return True
                mask |= 1 << num
            return False
        
        cnt = 0
        for i in range(1, n + 1):
            if is_special(i):
                cnt += 1
        return cnt
    
    def numDupDigitsAtMostN2(self, n: int) -> int:
        def count_unique_numbers(m: int) -> int:
            digits = list(map(int, str(m)))
            length = len(digits)
            count = 0
            
            # Count numbers with fewer digits than m
            for i in range(1, length):
                count += 9 * perm(9, i - 1)
            
            # Count numbers with the same number of digits as m
            used = set()
            for i in range(length):
                start = 1 if i == 0 else 0
                for num in range(start, digits[i]):
                    if num not in used:
                        count += perm(9 - i, length - i - 1)
                if digits[i] in used:
                    break
                used.add(digits[i])
            else:
                count += 1
            
            return count
        
        def perm(n: int, k: int) -> int:
            if k == 0:
                return 1
            return n * perm(n - 1, k - 1)
        
        return n - count_unique_numbers(n)
    
    def numDupDigitsAtMostN(self, n: int) -> int:
        def count_unique_numbers(m: int) -> int:
            digits = list(map(int, str(m)))
            length = len(digits)
            count = 0
            
            # Count numbers with fewer digits than m
            for i in range(1, length):
                count += 9 * math.perm(9, i - 1)
            
            # Count numbers with the same number of digits as m
            used = set()
            for i in range(length):
                start = 1 if i == 0 else 0
                for num in range(start, digits[i]):
                    if num not in used:
                        count += math.perm(9 - i, length - i - 1)
                if digits[i] in used:
                    break
                used.add(digits[i])
            else:
                count += 1
            
            return count
        
        return n - count_unique_numbers(n)