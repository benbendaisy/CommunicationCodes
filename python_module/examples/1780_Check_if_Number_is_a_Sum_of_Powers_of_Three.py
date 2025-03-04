import math
class Solution:
    """
    Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

    An integer y is a power of three if there exists an integer x such that y == 3x.

    Example 1:

    Input: n = 12
    Output: true
    Explanation: 12 = 31 + 32
    Example 2:

    Input: n = 91
    Output: true
    Explanation: 91 = 30 + 32 + 34
    Example 3:

    Input: n = 21
    Output: false
    """
    def checkPowersOfThree1(self, n: int) -> bool:
        @cache
        def helper(idx: int, running_sum: int) -> bool:
            if running_sum == n:
                return True
            if running_sum > n or idx > math.log(n, 3):
                return False
            
            return helper(idx + 1, running_sum) or helper(idx + 1, running_sum + 3 ** idx)
        
        return helper(0, 0)
    
    def checkPowersOfThree2(self, n: int) -> bool:
        if n == 0:
            return True
        
        if n % 3 == 2:
            return False
        
        return self.checkPowersOfThree(n // 3)
    
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            if n % 3 == 2:
                return False
            n = n // 3
        return True