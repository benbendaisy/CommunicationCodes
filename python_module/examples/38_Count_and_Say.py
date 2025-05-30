class Solution:
    """
        The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

        countAndSay(1) = "1"
        countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
        To determine how you "say" a digit string, split it into the minimal number of substrings such that each substring contains exactly one unique digit. Then for each substring, say the number of digits, then say the digit. Finally, concatenate every said digit.

        For example, the saying and conversion for digit string "3322251":

        Given a positive integer n, return the nth term of the count-and-say sequence.


        Example 1:

        Input: n = 1
        Output: "1"
        Explanation: This is the base case.
        Example 2:

        Input: n = 4
        Output: "1211"
        Explanation:
        countAndSay(1) = "1"
        countAndSay(2) = say "1" = one 1 = "11"
        countAndSay(3) = say "11" = two 1's = "21"
        countAndSay(4) = say "21" = one 2 + one 1 = "12" + "11" = "1211"
    """
    def countAndSay1(self, n: int) -> str:
        currentStr = "1"
        for _ in range(n - 1):
            nextStr = ""
            j = k = 0
            while j < len(currentStr):
                while k < len(currentStr) and currentStr[k] == currentStr[j]:
                    k += 1
                nextStr += str(k - j) + currentStr[j]
                j = k
            currentStr = nextStr
        return currentStr
    
    def countAndSay2(self, n: int) -> str:
        def helper(s: str, step: int) -> str:
            if step == n:
                return s
            idx, m, res = 0, len(s), ""
            while idx < m:
                cnt = 1
                while idx < m - 1 and s[idx] == s[idx + 1]:
                    cnt += 1
                    idx += 1
                res += str(cnt) + str(s[idx])
                idx += 1
            return helper(res, step + 1)
        return helper("1", 1)