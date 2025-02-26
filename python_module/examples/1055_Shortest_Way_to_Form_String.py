class Solution:
    """
    A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

    Given two strings source and target, return the minimum number of subsequences of source such that their concatenation equals target. If the task is impossible, return -1.

    Example 1:

    Input: source = "abc", target = "abcbc"
    Output: 2
    Explanation: The target "abcbc" can be formed by "abc" and "bc", which are subsequences of source "abc".
    Example 2:

    Input: source = "abc", target = "acdbc"
    Output: -1
    Explanation: The target string cannot be constructed from the subsequences of source string due to the character "d" in target string.
    Example 3:

    Input: source = "xyz", target = "xzyxz"
    Output: 3
    Explanation: The target string can be constructed as follows "xz" + "y" + "xz".
    """
    def shortestWay(self, source: str, target: str) -> int:
        if not source or not target:
            return 0
        # To check if target characters exist in source
        source_set = set(source)
        # If a character in target is missing from source, return -1
        for ch in target:
            if ch not in source_set:
                return -1
        # Number of times source is used and Pointer for target
        j, cnt = 0, 0
        while j < len(target):
            # Reset source pointer
            i = 0
            # Start a new subsequence from source
            cnt += 1
            while i < len(source) and j < len(target):
                # Match character in target
                if source[i] == target[j]:
                    # Move to next character in target
                    j += 1
                # Move to next character in source
                i += 1
        return cnt