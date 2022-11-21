from functools import lru_cache


class Solution:
    """
        Given a string s of lower and upper case English letters.

        A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

        0 <= i <= s.length - 2
        s[i] is a lower-case letter and s[i + 1] is the same letter but in upper-case or vice-versa.
        To make the string good, you can choose two adjacent characters that make the string bad and remove them. You can keep doing this until the string becomes good.

        Return the string after making it good. The answer is guaranteed to be unique under the given constraints.

        Notice that an empty string is also good.

        Example 1:

        Input: s = "leEeetcode"
        Output: "leetcode"
        Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".
        Example 2:

        Input: s = "abBAcC"
        Output: ""
        Explanation: We have many possible scenarios, and all lead to the same answer. For example:
        "abBAcC" --> "aAcC" --> "cC" --> ""
        "abBAcC" --> "abBA" --> "aA" --> ""
        Example 3:

        Input: s = "s"
        Output: "s"
    """
    @lru_cache(None)
    def makeGood1(self, s: str) -> str:
        if len(s) < 2:
            return s
        for i in range(len(s) - 1):
            if abs(ord(s[i]) - ord(s[i + 1])) == 32:
                return self.makeGood1(s[:i] + s[i + 2:])
        return s

    def makeGood(self, s: str) -> str:
        if len(s) < 2:
            return s

        # if s has less than 2 characters, we just return itself.
        while len(s) > 1:
            # 'find' records if we find any pair to remove.
            find = False
            # Check every two adjacent characters, curr_char and next_char.
            for i in range(len(s) - 1):
                # If they make a pair, remove them from 's' and let 'find = True'.
                if abs(ord(s[i]) - ord(s[i + 1])) == 32:
                    s = s[:i] + s[i + 2:]
                    find = True
                    break
            # If we cannot find any pair to remove, break the loop.
            if not find:
                return s
        return s
