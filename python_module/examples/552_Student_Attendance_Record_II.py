class Solution:
    """
    An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

    'A': Absent.
    'L': Late.
    'P': Present.
    Any student is eligible for an attendance award if they meet both of the following criteria:

    The student was absent ('A') for strictly fewer than 2 days total.
    The student was never late ('L') for 3 or more consecutive days.
    Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

    Example 1:

    Input: n = 2
    Output: 8
    Explanation: There are 8 records with length 2 that are eligible for an award:
    "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
    Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).
    Example 2:

    Input: n = 1
    Output: 3
    Example 3:

    Input: n = 10101
    Output: 183236316
    """
    def checkRecord1(self, n: int) -> int:
        """
        Memory Limit Exceeded
        """
        def valid(s: str):
            if not s:
                return True
            # rule 1
            if s.count("A") >= 2:
                return False
            
            # rule 2
            if "LLL" in s:
                return False
            return True
        
        res = set()
        mod = 10 ** 9 + 7
        @cache
        def helper(s):
            if len(s) == n:
                if valid(s):
                    res.add(s)
                return
            
            if s.count("A") >= 2:
                return
            
            if "LLL" in s:
                return
            
            for ch in ("A", "L", "P"):
                helper(s + ch)
        
        helper("")
        return len(res) % mod
    

    def checkRecord2(self, n: int) -> int:
        
        mod = 10 ** 9 + 7

        @cache
        def helper(idx: int, abscences: int, consecutive_late: int):
            if abscences >= 2 or consecutive_late >= 3:
                return 0
            
            if idx == n:
                return 1
            
            return (helper(idx + 1, abscences, 0) + helper(idx + 1, abscences + 1, 0) + helper(idx + 1, abscences, consecutive_late + 1)) % mod

        return helper(0, 0, 0)
    
    def checkRecord2(self, n: int) -> int:
        MOD = 10**9 + 7
    
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1  # Base case
        
        for i in range(n):
            for absences in range(2):
                for consecutive_lates in range(3):
                    # Adding 'P'
                    dp[i + 1][absences][0] = (dp[i + 1][absences][0] + dp[i][absences][consecutive_lates]) % MOD
                    
                    # Adding 'A'
                    if absences < 1:
                        dp[i + 1][absences + 1][0] = (dp[i + 1][absences + 1][0] + dp[i][absences][consecutive_lates]) % MOD
                    
                    # Adding 'L'
                    if consecutive_lates < 2:
                        dp[i + 1][absences][consecutive_lates + 1] = (dp[i + 1][absences][consecutive_lates + 1] + dp[i][absences][consecutive_lates]) % MOD
        
        return sum(dp[n][a][l] for a in range(2) for l in range(3)) % MOD
    
    def checkRecord2(self, n: int) -> int:
        mod = 10 ** 9 + 7
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]
        dp[0][0][0] = 1 # Base case

        for i in range(n):
            for absc in range(2):
                for la in range(3):
                    # adding "P"
                    dp[i + 1][absc][0] = (dp[i + 1][absc][0] + dp[i][absc][la]) % mod
                    # adding "A"
                    if absc < 1:
                        dp[i + 1][absc + 1][0] = (dp[i + 1][absc + 1][0] + dp[i][absc][la]) % mod
                    # adding "L"
                    if la < 2:
                        dp[i + 1][absc][la + 1] = (dp[i + 1][absc][la + 1] + dp[i][absc][la])
        
        return sum(dp[n][a][l] for a in range(2) for l in range(3)) % mod
    
    def checkRecord(self, n: int) -> int:
        
        mod = 10**9 + 7
    
        @lru_cache(None)
        def helper(idx, absences, consecutive_lates):
            if absences >= 2 or consecutive_lates >= 3:
                return 0  # Invalid record
            if idx == n:
                return 1  # Valid record of length 0
            
            # Choices: 'P', 'A', 'L'
            return (
                helper(idx + 1, absences, 0) +  # Adding 'P'
                helper(idx + 1, absences + 1, 0) +  # Adding 'A'
                helper(idx + 1, absences, consecutive_lates + 1)  # Adding 'L'
            ) % mod
        
        return helper(0, 0, 0)