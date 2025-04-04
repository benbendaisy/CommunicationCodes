from functools import lru_cache


class Solution:
    """
        Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

        An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

        s = s1 + s2 + ... + sn
        t = t1 + t2 + ... + tm
        |n - m| <= 1
        The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
        Note: a + b is the concatenation of strings a and b.

        Example 1:

        Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
        Output: true
        Example 2:

        Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
        Output: false
        Example 3:

        Input: s1 = "", s2 = "", s3 = ""
        Output: true
    """
    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2 = len(s1), len(s2)
        @lru_cache(None)
        def try_combination(ptr1, ptr2, res):
            if ptr1 == n1 and ptr2 == n2 and res == s3:
                return True
            ans = False
            if ptr1 < n1:
                ans = ans or try_combination(ptr1 + 1, ptr2, res + s1[ptr1])
            if ptr2 < n2:
                ans = ans or try_combination(ptr1, ptr2 + 1, res + s2[ptr2])
            return ans
        return try_combination(0, 0, "")

    def isInterleave3(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        memory = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        def tryAllCombinations(ptr1: int, ptr2: int):
            if ptr1 == len(s1):
                return s2[ptr2:] == s3[ptr1 + ptr2:]
            if ptr2 == len(s2):
                return s1[ptr1:] == s3[ptr1 + ptr2:]

            if memory[ptr1][ptr2] >= 0:
                return True if memory[ptr1][ptr2] == 1 else False

            ans = (s1[ptr1] == s3[ptr1 + ptr2] and tryAllCombinations(ptr1 + 1, ptr2)) or (s2[ptr2] == s3[ptr1 + ptr2] and tryAllCombinations(ptr1, ptr2 + 1))
            memory[ptr1][ptr2] = 1 if ans else 0
            return ans
        return tryAllCombinations(0, 0)

    def isInterleave4(self, s1: str, s2: str, s3: str) -> bool:
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False
        dp = [[False] * (n2 + 1) for _ in range(n1 + 1)]
        for i in range(n1 + 1):
            for j in range(n2 + 1):
                if i == 0 and j == 0:
                    dp[i][j] = True
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                else:
                    dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]) or (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])
        return dp[-1][-1]

    def isInterleave5(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True
        m, n, k = len(s1), len(s2), len(s3)

        @cache
        def helper(idx1: int, idx2: int, idx3: int) -> bool:
            if idx1 == m and idx2 == n:
                return idx3 == k
            
            if idx3 == k:
                return False
            
            if idx1 == m:
                return s2[idx2:] == s3[idx3:]
            
            if idx2 == n:
                return s1[idx1:] == s3[idx3:]
            
            if s1[idx1] == s3[idx3] and s2[idx2] == s3[idx3]:
                return helper(idx1 + 1, idx2, idx3 + 1) or helper(idx1, idx2 + 1, idx3 + 1)
            elif s1[idx1] == s3[idx3]:
                return helper(idx1 + 1, idx2, idx3 + 1)
            elif s2[idx2] == s3[idx3]:
                return helper(idx1, idx2 + 1, idx3 + 1)
            
            return False
        
        return helper(0, 0, 0)
    
    def isInterleave6(self, s1: str, s2: str, s3: str) -> bool:
        if not s1 and not s2 and not s3:
            return True
        if len(s1) + len(s2) != len(s3):
            return False
        
        m, n, k = len(s1), len(s2), len(s3)
        @cache
        def helper(idx1: int, idx2: int, idx3: int) -> bool:
            if idx1 == m and idx2 == n:
                return True
            
            if idx1 < m and s1[idx1] == s3[idx3] and helper(idx1 + 1, idx2, idx3 + 1):
                return True
            
            if idx2 < n and s2[idx2] == s3[idx3] and helper(idx1, idx2 + 1, idx3 + 1):
                return True
            
            return False
        return helper(0, 0, 0)

if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    solution = Solution()
    ret = solution.isInterleave(s1, s2, s3)
    print(ret)