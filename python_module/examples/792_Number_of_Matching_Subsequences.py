import collections
from functools import lru_cache
from typing import List


class Solution:
    """
        Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

        A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

        For example, "ace" is a subsequence of "abcde".

        Example 1:

        Input: s = "abcde", words = ["a","bb","acd","ace"]
        Output: 3
        Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
        Example 2:

        Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
        Output: 2

        Constraints:

        1 <= s.length <= 5 * 104
        1 <= words.length <= 5000
        1 <= words[i].length <= 50
        s and words[i] consist of only lowercase English letters.
    """
    def numMatchingSubseq1(self, s: str, words: List[str]) -> int:
        subSeqSet = set()
        @lru_cache(None)
        def findAllSubseqs(idx: int, subStr: str):
            if idx == len(s):
                subSeqSet.add(subStr)
                return

            findAllSubseqs(idx + 1, subStr + s[idx])
            findAllSubseqs(idx + 1, subStr)
        findAllSubseqs(0, "")
        cnt = 0
        for x in words:
            if x in subSeqSet:
                cnt += 1
        return cnt

    def numMatchingSubseq2(self, s: str, words: List[str]) -> int:
        waiting = collections.defaultdict(list)
        for w in words:
            waiting[w[0]].append(iter(w[1:]))
        for c in s:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])

    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        waiting = collections.defaultdict(list)
        for it in map(iter, words):
            waiting[next(it)].append(it)
        for c in s:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])

if __name__ == "__main__":
    s = "abcde"
    words = ["a","bb","acd","ace"]
    solution = Solution()
    ret = solution.numMatchingSubseq2(s, words)
    print(ret)