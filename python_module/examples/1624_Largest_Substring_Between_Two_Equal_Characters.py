class Solution:
    """
    Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.

    A substring is a contiguous sequence of characters within a string.

    Example 1:

    Input: s = "aa"
    Output: 0
    Explanation: The optimal substring here is an empty substring between the two 'a's.
    Example 2:

    Input: s = "abca"
    Output: 2
    Explanation: The optimal substring here is "bc".
    Example 3:

    Input: s = "cbzxy"
    Output: -1
    Explanation: There are no characters that appear twice in s.
    """
    def maxLengthBetweenEqualCharacters1(self, s: str) -> int:
        res = -1
        n = len(s)
        for l in range(n):
            for r in range(l + 1, n):
                if s[l] == s[r]:
                    res = max(res, r - l - 1)
        return res
    
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        first_idx = {}
        res = -1
        n = len(s)
        for i in range(n):
            if s[i] in first_idx:
                res = max(res, i - first_idx[s[i]] - 1)
            else:
                first_idx[s[i]] = i
        return res