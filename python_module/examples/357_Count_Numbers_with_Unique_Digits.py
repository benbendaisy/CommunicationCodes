class Solution:
    def countNumbersWithUniqueDigits1(self, n: int) -> int:
        def f(k):
            if k == 0: return 1
            res, cur = 9, 9
            while k > 1:
                res *= cur
                cur -= 1
                k -= 1
            return res
        res = 0
        for i in range(n+1):
            res += f(i)
        return res

    def countNumbersWithUniqueDigits2(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10
        
        total = 10  # Count for n=1
        current_options = 9  # Options for the first digit (1-9)
        available_digits = 9  # Remaining digits (0-9 except the first digit)
        
        for i in range(2, n + 1):
            current_options *= available_digits
            total += current_options
            available_digits -= 1
        
        return total
    
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 10
        total, current_options, available_digits = 10, 9, 9

        for _ in range(2, n + 1):
            current_options *= available_digits
            total += current_options
            available_digits -= 1
        return total