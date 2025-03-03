class Solution:
    """
    Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

    A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.

    Example 1:

    Input: str1 = "abac", str2 = "cab"
    Output: "cabac"
    Explanation: 
    str1 = "abac" is a subsequence of "cabac" because we can delete the first "c".
    str2 = "cab" is a subsequence of "cabac" because we can delete the last "ac".
    The answer provided is the shortest such string that satisfies these properties.
    """
    def shortestCommonSupersequence1(self, str1: str, str2: str) -> str:
        @cache
        def scs(i: int, j: int) -> str:
            if i == 0:  # If str1 is empty, return str2
                return str2[:j]
            if j == 0:  # If str2 is empty, return str1
                return str1[:i]
            
            if str1[i - 1] == str2[j - 1]:  # If characters match, include them in the result
                return scs(i - 1, j - 1) + str1[i - 1]
            
            # Otherwise, choose the shorter sequence by trying both options
            option1 = scs(i - 1, j) + str1[i - 1]
            option2 = scs(i, j - 1) + str2[j - 1]
            
            return option1 if len(option1) < len(option2) else option2
        
        return scs(len(str1), len(str2))
    
    def shortestCommonSupersequence2(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)
    
        # Create DP table for LCS
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # Construct the shortest common supersequence
        i, j = m, n
        result = []
        
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                # If the characters match, include only once in result
                result.append(str1[i - 1])
                i -= 1
                j -= 1
            elif dp[i - 1][j] > dp[i][j - 1]:
                # Include character from str1
                result.append(str1[i - 1])
                i -= 1
            else:
                # Include character from str2
                result.append(str2[j - 1])
                j -= 1
        
        # Include remaining characters from str1
        while i > 0:
            result.append(str1[i - 1])
            i -= 1
        
        # Include remaining characters from str2
        while j > 0:
            result.append(str2[j - 1])
            j -= 1
        
        # Reverse the result and join to get the final string
        return ''.join(result[::-1])
    

    def shortestCommonSupersequence3(self, str1: str, str2: str) -> str:
        if not str1 and not str2:
            return ""
        
        m, n = len(str1), len(str2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        i, j = m, n
        res = []
        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:
                res.append(str1[i - 1])
                i -= 1
                j -= 1
            else:
                if dp[i - 1][j] > dp[i][j - 1]:
                    res.append(str1[i - 1])
                    i -= 1
                else:
                    res.append(str2[j - 1])
                    j -= 1

        while i > 0:
            res.append(str1[i - 1])
            i -= 1
        
        while j > 0:
            res.append(str2[j - 1])
            j -= 1
        
        return "".join(res[::-1])
    
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        """
        Memory Limit Exceeded
        """
        if not str1 and not str2:
            return ""
        
        m, n = len(str1), len(str2)
        @cache
        def helper(idx1: int, idx2:int):
            if idx1 == m:
                return str2[idx2:]
            if idx2 == n:
                return str1[idx1:]
            
            if str1[idx1] == str2[idx2]:
                return str1[idx1] + helper(idx1 + 1, idx2 + 1)
            
            option1 = str1[idx1] + helper(idx1 + 1, idx2)
            option2 = str2[idx2] + helper(idx1, idx2 + 1)
            return option1 if len(option1) < len(option2) else option2
        
        return helper(0, 0)