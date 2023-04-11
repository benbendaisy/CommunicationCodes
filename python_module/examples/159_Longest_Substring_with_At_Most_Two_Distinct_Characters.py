from collections import defaultdict


class Solution:
    """
        Given a string s, return the length of the longest substring that
        contains at most two distinct characters.

        Example 1:

        Input: s = "eceba"
        Output: 3
        Explanation: The substring is "ece" which its length is 3.
        Example 2:

        Input: s = "ccaabbb"
        Output: 5
        Explanation: The substring is "aabbb" which its length is 5.


        Constraints:
        
        1 <= s.length <= 105
        s consists of English letters.
    """

    def lengthOfLongestSubstringTwoDistinct1(self, s: str) -> int:
        if not s:
            return 0
        l = r = 0
        hash_map = {}
        max_length = 1
        while r < len(s):
            hash_map[s[r]] = r
            if len(hash_map) == 3:
                min_index = min(hash_map.values())
                del hash_map[s[min_index]]
                l = min_index + 1
            max_length = max(max_length, r - l + 1)
            r += 1
        return max_length

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        running window
        :param s:
        :return:
        """
        if not s:
            return 0
        chars_dict = defaultdict(int)
        start = 0
        res = 0
        for i, v in enumerate(s):
            chars_dict[s[i]] += 1
            while len(chars_dict) > 2:
                chars_dict[s[start]] -= 1
                if chars_dict[s[start]] == 0:
                    del chars_dict[s[start]]
                start += 1
            res = max(res, i - start + 1)
        return res

if __name__ == "__main__":
    s = "cacaabbb"
    solution = Solution()
    ret = solution.lengthOfLongestSubstringTwoDistinct(s)
    print(ret)