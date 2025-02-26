import functools
from collections import defaultdict
from typing import List


class Solution:
    def minCut1(self, s: str) -> int:
        n = len(s)
        if not s or n == 1:
            return 0
        if n == 2:
            return 0 if s[0] == s[1] else 1

        cut = n
        if s[0] == s[n - 1]:
            cut = self.minCut(s[1 : n - 1])
        else:
            cut = 1 + min(self.minCut(s[1 :]), self.minCut(s[: n - 1]))

        return cut

    def minCutWithCache(self, s: str, memory: List):
        length = len(s)
        if length <= 1:
            return 0
        elif length == 2:
            return 0 if s[0] == s[1] else 1
        elif memory[s] >= 0:
            return memory[s]
        elif s == s[::-1]:
            memory[s] = 0
            return 0

        cut = length
        for i in range(1, length):
            st = s[:i]
            if st == st[::-1]:
                cut = min(cut, 1 + self.minCutWithCache(s[i:], memory))
        memory[s] = cut
        return cut

    def minCut2(self, s: str) -> int:
        memory = defaultdict(lambda:-1)
        return self.minCutWithCache(s, memory)
    
    def minCut3(self, s: str) -> int:
        if not s:
            return 0
        elif len(s) < 2:
            return 0
        n = len(s)
        def check_palin(str1: str):
            return str1 == str1[::-1]
        @cache
        def helper(idx: int, cut: int):
            if idx == n:
                return cut - 1
            
            min_cut = float("inf")
            for i in range(idx, n):
                if check_palin(s[idx:i + 1]):
                    min_cut = min(min_cut, helper(i + 1, cut + 1))
            return min_cut
        return helper(0, 0)
    
    def minCut(self, s: str) -> int:
        n = len(s)
    
        # dp[i] represents the minimum cuts needed for s[i:n]
        dp = [-1] * n
        
        # is_palindrome[i][j] indicates whether s[i:j+1] is a palindrome
        is_palindrome = [[False] * n for _ in range(n)]
        
        # Pre-compute all palindromes in the string
        for i in range(n):
            for j in range(i + 1):
                if s[i] == s[j] and (i - j <= 2 or is_palindrome[j + 1][i - 1]):
                    is_palindrome[j][i] = True
        
        def min_cuts_helper(start):
            # Base case: If we've reached the end of the string
            if start >= n:
                return 0
            
            # If we already computed this value
            if dp[start] != -1:
                return dp[start]
            
            # If the entire remaining substring is a palindrome, no cuts needed
            if is_palindrome[start][n-1]:
                return 0
            
            # Initialize with worst case (cut after each character)
            min_cuts = float('inf')
            
            # Try all possible ending positions for the first palindrome
            for end in range(start, n):
                if is_palindrome[start][end]:
                    cuts = 1 + min_cuts_helper(end + 1)
                    min_cuts = min(min_cuts, cuts)
            
            # Store the result in our dp table
            dp[start] = min_cuts
            return min_cuts
        
        return min_cuts_helper(0)

if __name__ == "__main__":
    s = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
    solution = Solution()
    ret = solution.minCut(s)
    print(ret)