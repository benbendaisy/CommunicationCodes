from collections import Counter


class Solution:
    """
        Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

        Example 1:

        Input: s = "bcabc"
        Output: "abc"
        Example 2:

        Input: s = "cbacdcbc"
        Output: "acdb"

        Constraints:

        1 <= s.length <= 104
        s consists of lowercase English letters.
    """
    def removeDuplicateLetters(self, s: str) -> str:
        lastIndexes = {ch:i for i,ch in enumerate(s)}
        stack = []
        visited = set()
        for i in range(len(s)):
            if s[i] not in visited:
                while stack and s[i] < stack[-1] and lastIndexes[s[i]] > i:
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])
        return "".join(stack)
