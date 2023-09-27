class Solution:
    """
    implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

    The algorithm for myAtoi(string s) is as follows:

    Read in and ignore any leading whitespace.
    Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
    Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
    Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
    If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
    Return the integer as the final result.
    """
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1
        pos, neg = False, False

        if i < n and s[i] == '-':
            neg = True
            i += 1
        if i < n and s[i] == '+':
            pos = True
            i += 1
        ans = 0.0
        while i < n and '0' <= s[i] <= '9':
            ans = ans * 10 + (ord(s[i]) - ord('0'))
            i += 1
        if neg:
            ans = -ans
        if pos and neg:
            return 0
        int_max = 2 ** 31 - 1
        int_min = -2 ** 31
        if ans > int_max:
            ans = int_max
        if ans < int_min:
            ans = int_min
        return int(ans)
            