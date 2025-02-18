class Solution:
    """
    Given a string s, return the maximum number of unique substrings that the given string can be split into.

    You can split string s into any list of non-empty substrings, where the concatenation of the substrings forms the original string. However, you must split the substrings such that all of them are unique.

    A substring is a contiguous sequence of characters within a string.

    Example 1:

    Input: s = "ababccc"
    Output: 5
    Explanation: One way to split maximally is ['a', 'b', 'ab', 'c', 'cc']. Splitting like ['a', 'b', 'a', 'b', 'c', 'cc'] is not valid as you have 'a' and 'b' multiple times.
    Example 2:

    Input: s = "aba"
    Output: 2
    Explanation: One way to split maximally is ['a', 'ba'].
    Example 3:

    Input: s = "aa"
    Output: 1
    Explanation: It is impossible to split the string any further.
    """
    def maxUniqueSplit(self, s: str) -> int:
        if not s:
            return 0
        max_length = 0
        def back_track(path: set, idx: int):
            nonlocal max_length
            if idx == len(s):
                max_length = max(max_length, len(path))
                return
            for i in range(idx, len(s)):
                if s[idx:i + 1] not in path:
                    path.add(s[idx:i + 1])
                    back_track(path, i + 1)
                    path.discard(s[idx:i + 1])
        back_track(set(), 0)
        return max_length