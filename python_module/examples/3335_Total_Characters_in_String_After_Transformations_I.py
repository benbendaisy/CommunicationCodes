class Solution:
    """
    You are given a string s and an integer t, representing the number of transformations to perform. In one transformation, every character in s is replaced according to the following rules:

    If the character is 'z', replace it with the string "ab".
    Otherwise, replace it with the next character in the alphabet. For example, 'a' is replaced with 'b', 'b' is replaced with 'c', and so on.
    Return the length of the resulting string after exactly t transformations.

    Since the answer may be very large, return it modulo 109 + 7.
    
    Example 1:

    Input: s = "abcyy", t = 2

    Output: 7

    Explanation:

    First Transformation (t = 1):
    'a' becomes 'b'
    'b' becomes 'c'
    'c' becomes 'd'
    'y' becomes 'z'
    'y' becomes 'z'
    String after the first transformation: "bcdzz"
    Second Transformation (t = 2):
    'b' becomes 'c'
    'c' becomes 'd'
    'd' becomes 'e'
    'z' becomes "ab"
    'z' becomes "ab"
    String after the second transformation: "cdeabab"
    Final Length of the string: The string is "cdeabab", which has 7 characters.
    Example 2:

    Input: s = "azbk", t = 1

    Output: 5

    Explanation:

    First Transformation (t = 1):
    'a' becomes 'b'
    'z' becomes "ab"
    'b' becomes 'c'
    'k' becomes 'l'
    String after the first transformation: "babcl"
    Final Length of the string: The string is "babcl", which has 5 characters.
    """
    def lengthAfterTransformations1(self, s: str, t: int) -> int:
        """
        Time limit exceeded
        """
        mod = 10 ** 9 + 7
        t_dict = {
            "a": "b", "b": "c", "c": "d", "d": "e", "e": "f", "f": "g", "g": "h",
            "h": "i", "i": "j", "j": "k", "k": "l", "l": "m", "m": "n", "n": "o",
            "o": "p", "p": "q", "q": "r", "r": "s", "s": "t", "t": "u", "u": "v", 
            "v": "w", "w": "x", "x": "y", "y": "z", "z": "ab"
        }

        while t > 0:
            new_s = ""
            for ch in s:
                new_s += t_dict[ch]
            s = new_s
            t -= 1
        return len(s) % mod
    
    def lengthAfterTransformations2(self, s: str, t: int) -> int:
        mod = 10**9 + 7
        cnt = [0] * 26
        for ch in s:
            cnt[ord(ch) - ord("a")] += 1
        for round in range(t):
            nxt = [0] * 26
            nxt[0] = cnt[25]
            nxt[1] = (cnt[25] + cnt[0]) % mod
            for i in range(2, 26):
                nxt[i] = cnt[i - 1]
            cnt = nxt
        ans = sum(cnt) % mod
        return ans