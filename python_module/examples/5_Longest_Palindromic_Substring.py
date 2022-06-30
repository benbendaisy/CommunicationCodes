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

    def longestPalindrome(self, s: str) -> str:
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


if __name__ == "__main__":
    s = "boqylncwfahjzvawrojyhqiymirlkfzkhtvmbjnbfjxzewqqqcfnximdnrxtrbafkimcqvuprgrjetrecqkltforcudmbpofcxqdcirnaciggflvsialdjtjnbrayeguklcbdbkouodxbmhgtaonzqftkebopghypjzfyqutytbcfejhddcrinopynrprohpbllxvhitazsjeyymkqkwuzfenhphqfzlnhenldbigzmriikqkgzvszztmvylzhbfjoksyvfdkvshjzdleeylqwsapapduxrfbwskpnhvmagkolzlhakvfbvcewvdihqceecqhidvwecvbfvkahlzlokgamvhnpkswbfrxudpapaswqlyeeldzjhsvkdfvyskojfbhzlyvmtzzsvzgkqkiirmzgibdlnehnlzfqhphnefzuwkqkmyyejszatihvxllbphorprnyponircddhjefcbtytuqyfzjpyhgpobektfqznoatghmbxdouokbdbclkugeyarbnjtjdlaisvlfggicanricdqxcfopbmducroftlkqcertejrgrpuvqcmikfabrtxrndmixnfcqqqwezxjfbnjbmvthkzfklrimyiqhyjorwavzjhafwcnlyqob"
    solution = Solution()
    ret = solution.longestPalindrome(s)
    print(ret)