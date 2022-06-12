class Solution:
    """
        Given a pattern and a string s, return true if s matches the pattern.

        A string s matches a pattern if there is some bijective mapping of single characters to strings such that if each character in pattern is replaced by the string it maps to, then the resulting string is s. A bijective mapping means that no two characters map to the same string, and no character maps to two different strings.

        Example 1:

        Input: pattern = "abab", s = "redblueredblue"
        Output: true
        Explanation: One possible mapping is as follows:
        'a' -> "red"
        'b' -> "blue"
        Example 2:

        Input: pattern = "aaaa", s = "asdasdasdasd"
        Output: true
        Explanation: One possible mapping is as follows:
        'a' -> "asd"
        Example 3:

        Input: pattern = "aabb", s = "xyzabcxzyabc"
        Output: false

        Constraints:

        1 <= pattern.length, s.length <= 20
        pattern and s consist of only lowercase English letters.
    """
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        def backTrack(pIdx: int, sIdx: int, pDict: dict, sDict: dict) -> bool:
            lp, ls = len(pattern), len(s)
            if pIdx == lp and sIdx == ls:
                return True
            elif pIdx == lp or sIdx == ls:
                return False

            res, curPatternChar = False, pattern[pIdx]
            for i in range(sIdx, ls):
                subStr = s[sIdx : i + 1]
                if curPatternChar in pDict:
                    if pDict[curPatternChar] == subStr:
                        res = res | backTrack(pIdx + 1, i + 1, pDict, sDict)
                elif subStr not in sDict:
                    pDict[curPatternChar] = subStr
                    sDict[subStr] = curPatternChar
                    res = res | backTrack(pIdx + 1, i + 1, pDict, sDict)
                    del pDict[curPatternChar]
                    del sDict[subStr]
            return res

        return backTrack(0, 0, {}, {})


