class Solution:
    """
    Given a pattern and a string s, find if s follows the same pattern.

    Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s. Specifically:

    Each letter in pattern maps to exactly one unique word in s.
    Each unique word in s maps to exactly one letter in pattern.
    No two letters map to the same word, and no two words map to the same letter.
    
    Example 1:

    Input: pattern = "abba", s = "dog cat cat dog"

    Output: true

    Explanation:

    The bijection can be established as:

    'a' maps to "dog".
    'b' maps to "cat".
    Example 2:

    Input: pattern = "abba", s = "dog cat cat fish"

    Output: false

    Example 3:

    Input: pattern = "aaaa", s = "dog cat cat dog"

    Output: false
    """
    def wordPattern1(self, pattern: str, s: str) -> bool:
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
    
    def wordPattern2(self, pattern: str, s: str) -> bool:
        def transform(str1: list):
            idx_dict = {}
            new_str = []
            for i, v in enumerate(str1):
                if v not in idx_dict:
                    idx_dict[v] = i
                new_str.append(str(idx_dict[v]))
            return " ".join(new_str)
        
        return transform(list(pattern)) == transform(s.split())

if __name__ == "__main__":
    pattern = "abba"
    s = "dog cat cat dog"
    solution = Solution()
    ret = solution.wordPattern(pattern, s)
    print(ret)