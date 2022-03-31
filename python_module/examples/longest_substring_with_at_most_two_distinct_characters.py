from collections import defaultdict


class Solution:
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