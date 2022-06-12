from collections import defaultdict


class Solution:
    """
        Given a string s, find the length of the longest substring without repeating characters.

        Example 1:

        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.
        Example 2:

        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.
        Example 3:

        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


        Constraints:

        0 <= s.length <= 5 * 104
        s consists of English letters, digits, symbols and spaces.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        walker = runner = 0
        seen = set()
        maxLength = 0
        while runner < len(s):
            while s[runner] in seen:
                seen.remove(s[walker])
                walker += 1
            seen.add(s[runner])
            maxLength = max(maxLength, runner - walker + 1)
            runner += 1

        maxLength = max(maxLength, runner - walker)
        return maxLength


if __name__ == "__main__":
    s = "abba"
    solution = Solution()
    ret = solution.lengthOfLongestSubstring(s)
    print(ret)
