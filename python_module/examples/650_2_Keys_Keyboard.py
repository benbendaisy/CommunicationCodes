class Solution:
    """
    There is only one character 'A' on the screen of a notepad. You can perform one of two operations on this notepad for each step:

    Copy All: You can copy all the characters present on the screen (a partial copy is not allowed).
    Paste: You can paste the characters which are copied last time.
    Given an integer n, return the minimum number of operations to get the character 'A' exactly n times on the screen.

    Example 1:

    Input: n = 3
    Output: 3
    Explanation: Initially, we have one character 'A'.
    In step 1, we use Copy All operation.
    In step 2, we use Paste operation to get 'AA'.
    In step 3, we use Paste operation to get 'AAA'.
    Example 2:

    Input: n = 1
    Output: 0
    """
    def minSteps1(self, n: int) -> int:
        @cache
        def helper(x: int) -> int:
            if x == 1:
                return 0
            
            for factor in range(2, x + 1):
                if  x % factor == 0:
                    return helper(x // factor) + factor
        
        return helper(n)
    
    def minSteps2(self, n: int) -> int:
        if n == 1:
            return 0
        
        ops = 0
        while n > 1:
            for factor in range(2, n + 1):
                if n % factor == 0:
                    ops += factor
                    n = n // factor
                    break
        return ops
    
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0  # Edge case: No operations needed for "A"

        steps = 0
        factor = 2  # Start with the smallest prime factor

        while n > 1:
            while n % factor == 0:
                steps += factor
                n //= factor
            factor += 1  # Move to the next potential factor

        return steps