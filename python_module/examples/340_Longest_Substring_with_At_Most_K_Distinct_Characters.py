from collections import defaultdict


class Solution:
    """
        Given a string s and an integer k, return the length of the longest
        substring of s that contains at most k distinct characters.

        Example 1:

        Input: s = "eceba", k = 2
        Output: 3
        Explanation: The substring is "ece" with length 3.
        Example 2:

        Input: s = "aa", k = 1
        Output: 2
        Explanation: The substring is "aa" with length 2.


        Constraints:

        1 <= s.length <= 5 * 104
        0 <= k <= 50
    """
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or k < 1:
            return 0

        hashMap = defaultdict(lambda: 0)
        maxLength = 0
        l = 0
        for i in range(len(s)):
            hashMap[s[i]] = i
            if len(hashMap) == k + 1:
                minIndex = min(hashMap.values())
                del hashMap[s[minIndex]]
                l = minIndex + 1
            maxLength = max(maxLength, i - l + 1)

        return maxLength

if __name__ == "__main__":
    s = "ab"
    solution = Solution()
    ret = solution.lengthOfLongestSubstringKDistinct(s, 1)
    print(ret)