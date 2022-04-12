class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if not pattern or not s:
            return False

        words = [x for x in s.split()]
        if len(pattern) != len(words):
            return False

        charMap = {}
        wordMap = {}

        for c, w in zip(pattern, words):
            if c not in charMap:
                if w in wordMap:
                    return False
                else:
                    charMap[c] = w
                    wordMap[w] = c
            else:
                if charMap[c] != w:
                    return False
        return True

if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"
    solution = Solution()
    ret = solution.wordPattern(pattern, s)
    print(ret)