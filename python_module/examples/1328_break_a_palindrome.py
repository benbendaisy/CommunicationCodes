class Solution:
    def breakPalindrome1(self, palindrome: str) -> str:
        if not palindrome or len(palindrome) == 1:
            return ""

        chars = [x for x in palindrome]
        cur = 0
        while cur < len(palindrome)//2:
            if chars[cur] != 'a':
                chars[cur] = chr(ord(chars[cur]) - 1)
                return "".join(chars)
            cur += 1

        chars[len(palindrome) - 1] = 'b'
        return "".join(chars)

    def breakPalindrome(self, palindrome: str) -> str:
        if not palindrome or len(palindrome) == 1:
            return ""
        chars = list(palindrome)
        cur = 0
        while cur < len(chars) // 2:
            # change first non 'a' character to 'a'
            if chars[cur] != 'a':
                chars[cur] = 'a'
                return "".join(chars)
            cur += 1
        chars[len(palindrome) - 1] = 'b' # handle all characters are 'a's
        return "".join(chars)




if __name__ == "__main__":
    s = "aa"
    solution = Solution()
    ret = solution.breakPalindrome(s)
    print(ret)