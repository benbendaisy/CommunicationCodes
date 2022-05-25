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

    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0
        l = r = 0
        hashmap = defaultdict()
        maxLength = 1
        while r < len(s):
            hashmap[s[r]] = r
            r += 1
            if len(hashmap) == 3:
                minIndex = min(hashmap.values())
                del hashmap[s[minIndex]]
                l = minIndex + 1
            maxLength = max(maxLength, r - l)
        return maxLength


if __name__ == "__main__":
    s = "cacaabbb"
    solution = Solution()
    ret = solution.lengthOfLongestSubstringTwoDistinct(s)
    print(ret)