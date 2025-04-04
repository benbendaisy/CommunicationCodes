class Solution:
    """
        Given a string s, return the longest palindromic substring in s.

        Example 1:

        Input: s = "babad"
        Output: "bab"
        Explanation: "aba" is also a valid answer.
        Example 2:

        Input: s = "cbbd"
        Output: "bb"


        Constraints:

        1 <= s.length <= 1000
        s consist of only digits and English letters.
    """
    def longestPalindrome1(self, s: str) -> str:
        if not s:
            return s

        length = len(s)
        maxStr = ""
        for i in range(length):
            for j in range(i + 1, length):
                subStr = s[i:j]
                if subStr == subStr[::-1] and len(subStr) > len(maxStr):
                    maxStr = subStr
        return maxStr

    def longestPalindrome2(self, s: str) -> str:
        n = len(s)
        def expand(left:int, right:int):
            while 0 <= left <= right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return (left + 1, right)
        maxIndexes = (0, 0)
        for i in range(n):
            w1 = expand(i, i)
            w2 = expand(i, i + 1)
            maxIndexes = max(maxIndexes, w1, w2, key=lambda x: x[1] - x[0] + 1)
        return s[maxIndexes[0]:maxIndexes[1]]
    
    def longestPalindrome3(self, s: str) -> str:
        def expand_around_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]
        longest = ""
        for i in range(len(s)):
            palind1 = expand_around_center(i, i)
            palind2 = expand_around_center(i, i + 1)
            if len(palind1) > len(longest):
                longest = palind1
            if len(palind2) > len(longest):
                longest = palind2
        return longest
    
    def longestPalindrome4(self, s: str) -> str:
        
        n = len(s)
        # Form a bottom-up dp 2d array
        # dp[i][j] will be 'true' if the string from index i to j is a palindrome. 
        dp = [[False] * n  for _ in range(n)]
        
        ans = ''
        # every string with one character is a palindrome
        for i in range(n):
            dp[i][i] = True
            ans = s[i]
            
        maxLen = 1
        for start in range(n-1, -1, -1):
            for end in range(start+1, n):             
				# palindrome condition
                if s[start] == s[end]:
                    # if it's a two char. string or if the remaining string is a palindrome too
                    if end - start == 1 or dp[start+1][end-1]:
                        dp[start][end] = True
                        if maxLen < end - start + 1:
                            maxLen = end - start + 1
                            ans = s[start: end+ 1]
        
        return ans

    def longestPalindrome5(self, s: str) -> str:
        def check(i, j):
            left = i
            right = j - 1
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        for length in range(len(s), 0, -1):
            for start in range(len(s) - length + 1):
                if check(start, start + length):
                    return s[start:start + length]
        return ""
    
    def longestPalindrome6(self, s: str) -> str:
        n = len(s)
        def expand(l: int, r: int) -> str:
            if l < 0 or r >= n or s[l] != s[r]:
                return ""
            
            return expand(l - 1, r + 1) if l > 0 and r < n - 1 and s[l - 1] == s[r + 1] else s[l:r + 1] 
        
        max_pal = ""
        for i in range(n):
            # Odd length palindromes
            odd = expand(i, i)
            if len(odd) > len(max_pal):
                max_pal = odd
            # Even length palindromes
            even = expand(i, i + 1)
            if len(even) > len(max_pal):
                max_pal = even
        return max_pal
    
    def longestPalindrome7(self, s: str) -> str:
        n = len(s)

        def expand(left: int, right: int) -> int:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]
        
        max_len, max_str = float('-inf'), ""
        for i in range(n):
            # odd
            str1 = expand(i, i)
            if max_len < len(str1):
                max_len = len(str1)
                max_str = str1
            # even
            if i + 1 < n and s[i] == s[i + 1]:
                str1 = expand(i, i + 1)
                if max_len < len(str1):
                    max_len = len(str1)
                    max_str = str1
        return max_str

    def longestPalindrome8(self, s: str) -> str:
        n = len(s)

        def expand(left: int, right: int) -> int:
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1: right]
        
        max_str = ""
        for i in range(n):
            # odd
            str1 = expand(i, i)
        
            # even
            str2 = ""
            if i + 1 < n and s[i] == s[i + 1]:
                str2 = expand(i, i + 1)
            max_str = max(max_str, str1, str2, key=len)
        return max_str
    
if __name__ == "__main__":
    s = "boqylncwfahjzvawrojyhqiymirlkfzkhtvmbjnbfjxzewqqqcfnximdnrxtrbafkimcqvuprgrjetrecqkltforcudmbpofcxqdcirnaciggflvsialdjtjnbrayeguklcbdbkouodxbmhgtaonzqftkebopghypjzfyqutytbcfejhddcrinopynrprohpbllxvhitazsjeyymkqkwuzfenhphqfzlnhenldbigzmriikqkgzvszztmvylzhbfjoksyvfdkvshjzdleeylqwsapapduxrfbwskpnhvmagkolzlhakvfbvcewvdihqceecqhidvwecvbfvkahlzlokgamvhnpkswbfrxudpapaswqlyeeldzjhsvkdfvyskojfbhzlyvmtzzsvzgkqkiirmzgibdlnehnlzfqhphnefzuwkqkmyyejszatihvxllbphorprnyponircddhjefcbtytuqyfzjpyhgpobektfqznoatghmbxdouokbdbclkugeyarbnjtjdlaisvlfggicanricdqxcfopbmducroftlkqcertejrgrpuvqcmikfabrtxrndmixnfcqqqwezxjfbnjbmvthkzfklrimyiqhyjorwavzjhafwcnlyqob"
    solution = Solution()
    ret = solution.longestPalindrome(s)
    print(ret)