from functools import lru_cache


class Solution:
    def __init__(self):
        self.palSet = set()

    def countPalindromicSubsequences1(self, s: str) -> int:
        mod = 10**9 + 7

        @lru_cache(None)
        def countPalSub(str1: str):
            if not str1:
                return
            elif len(str1) == 1:
                self.palSet.add(str1)
                return
            elif str1 == str1[::-1]:
                self.palSet.add(str1)

            for i in range(len(str1)):
                countPalSub(str1[:i] + str1[i + 1:])

        countPalSub(s)
        return len(self.palSet) % mod

    def countPalindromicSubsequences2(self, s: str) -> int:
        resSet = set()
        def palindromicSubs(str1, str2):
            if len(str1) == 0:
                if str2 and str2 == str2[::-1]:
                    resSet.add(str2)
                return
            palindromicSubs(str1[1:], str2 + str1[0])
            palindromicSubs(str1[1:], str2)

        palindromicSubs(s, "")
        return len(resSet)
    
    def countPalindromicSubsequences3(self, s: str) -> int:
        mod = 10**9 + 7

        @lru_cache(None)
        def helper(left: int, right: int) -> int:
            if left > right:
                return 0
            if left == right:
                return 1  # A single character is a palindromic subsequence

            # Case 1: When s[left] == s[right]
            if s[left] == s[right]:
                l, r = left + 1, right - 1
                
                # Find the first and last occurrence of s[left] between (left+1, right-1)
                while l <= r and s[l] != s[left]: 
                    l += 1
                while l <= r and s[r] != s[left]: 
                    r -= 1

                if l > r:
                    count = 2 * helper(left + 1, right - 1) + 2  # No duplicate characters inside
                elif l == r:
                    count = 2 * helper(left + 1, right - 1) + 1  # One duplicate character inside
                else:
                    count = 2 * helper(left + 1, right - 1) - helper(l + 1, r - 1)  # Remove double-counting

            # Case 2: When s[left] != s[right]
            else:
                count = helper(left + 1, right) + helper(left, right - 1) - helper(left + 1, right - 1)

            return count % mod

        return helper(0, len(s) - 1)
    
    def countPalindromicSubsequences(self, s: str) -> int:
        n, mod = len(s), 10 ** 9 + 7
    
        @cache
        def helper(left: int, right: int) -> int:
            if left > right:
                return 0
            if left == right:
                return 1 # A single character is a palindromic subsequence
            
            # Case 1: When s[left] == s[right]
            if s[left] == s[right]:
                l, r = left + 1, right - 1
                # Find the first and last occurrence of s[left] between (left+1, right-1)
                while l <= r and s[l] != s[left]:
                    l += 1
                while r >= l and s[r] != s[right]:
                    r -= 1
                if l > r:
                    cnt = 2 * helper(left + 1, right - 1) + 2 # no duplication, # 's[i]' and 's[i]s[j]'
                elif l == r:
                    cnt = 2 * helper(left + 1, right - 1) + 1 # one duplication # 's[i]s[j]' and 's[i]' is already counted in helper(left + 1, right - 1)
                else:
                    cnt = 2 * helper(left + 1, right - 1) - helper(l + 1, r - 1) # more than one duplication and removing duplication where both cases are counted
            # Case 2: When s[left] != s[right]
            else:
                cnt = helper(left + 1, right) + helper(left, right - 1) - helper(left + 1, right - 1)
            return cnt % mod
        
        return helper(0, n - 1)
