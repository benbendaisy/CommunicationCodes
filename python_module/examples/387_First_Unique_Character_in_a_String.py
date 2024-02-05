from collections import defaultdict, Counter


class Solution:
    """
        Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

        Example 1:

        Input: s = "leetcode"
        Output: 0
        Example 2:

        Input: s = "loveleetcode"
        Output: 2
        Example 3:

        Input: s = "aabb"
        Output: -1

        Constraints:

        1 <= s.length <= 105
        s consists of only lowercase English letters.
    """
    def firstUniqChar1(self, s: str) -> int:
        if not s:
            return -1
        charMap = defaultdict(list)
        for i, v in enumerate(s):
            charMap[v].append(i)
        delKeys = []

        for key in charMap.keys():
            if len(charMap[key]) > 1:
                delKeys.append(key)

        for key in delKeys:
            del charMap[key]

        minChar = None
        minIndex = len(s)
        for key in charMap.keys():
            if charMap[key][0] < minIndex:
                minIndex = charMap[key][0]
                minChar = key
        return minChar

    def firstUniqChar2(self, s: str) -> int:
        if not s:
            return -1

        charMap = Counter(s)
        for i, v in enumerate(s):
            if charMap[v] == 1:
                return i
        return -1
    
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        cnt = Counter(s)
        for idx, ch in enumerate(s):
            if cnt[ch] == 1:
                return idx
        return -1
