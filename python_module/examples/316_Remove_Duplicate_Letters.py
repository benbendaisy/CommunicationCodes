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
    def removeDuplicateLetters1(self, s: str) -> str:
        last_indexes = {ch:i for i,ch in enumerate(s)}
        stack = []
        visited = set()
        for i in range(len(s)):
            if s[i] not in visited:
                # last_indexes[stack[-1]] > i proves there is another element later
                while stack and s[i] < stack[-1] and last_indexes[stack[-1]] > i:
                    visited.remove(stack.pop())
                stack.append(s[i])
                visited.add(s[i])
        return "".join(stack)

    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        letters_count = defaultdict(int)
        for ch in s:
            letters_count[ch] += 1
        for ch in s:
            if ch not in stack:
                while stack and stack[-1] > ch and letters_count[stack[-1]] > 0:
                    stack.pop()
                stack.append(ch)
            letters_count[ch] -= 1
        return "".join(stack)
        