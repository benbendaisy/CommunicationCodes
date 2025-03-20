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
    def lengthOfLongestSubstring1(self, s: str) -> int:
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

    def lengthOfLongestSubstring2(self, s: str) -> int:
        """
            Running window
        :param s:
        :return:
        """
        char_set = set()
        l, res = 0, 0
        for i, ch in enumerate(s):
            while ch in char_set:
                char_set.discard(s[l])
                l += 1
            char_set.add(ch)
            res = max(res, i - l + 1)
        return res
    
    def lengthOfLongestSubstring3(self, s: str) -> int:
        char_set = set()
        left, max_len = 0, 0
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)
        return max_len
    
    def lengthOfLongestSubstring4(self, s: str) -> int:
        window = []
        left, max_len = 0, 0
        for i, v in enumerate(s):
            while window and v in window:
                window.pop(0)
                left += 1
            window.append(v)
            max_len = max(max_len, i - left + 1)
        return max_len
    
    def lengthOfLongestSubstring5(self, s: str) -> int:
        window = set()
        left, max_len = 0, 0
        for i, v in enumerate(s):
            while window and v in window:
                window.remove(s[left])
                left += 1
            window.add(v)
            max_len = max(max_len, i - left + 1)
        return max_len


if __name__ == "__main__":
    s = "abba"
    solution = Solution()
    ret = solution.lengthOfLongestSubstring(s)
    print(ret)
