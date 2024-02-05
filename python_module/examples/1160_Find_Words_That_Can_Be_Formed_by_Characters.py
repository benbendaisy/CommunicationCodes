from typing import List


class Solution:
    """
    You are given an array of strings words and a string chars.

    A string is good if it can be formed by characters from chars (each character can only be used once).

    Return the sum of lengths of all good strings in words.

    Example 1:

    Input: words = ["cat","bt","hat","tree"], chars = "atach"
    Output: 6
    Explanation: The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
    Example 2:

    Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
    Output: 10
    Explanation: The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
    """
    def countCharacters1(self, words: List[str], chars: str) -> int:
        counts = defaultdict(int)
        for c in chars:
            counts[c] += 1
        res = 0
        for word in words:
            word_count = defaultdict(int)
            for c in word:
                word_count[c] += 1
            good = True
            for c, freq in word_count.items():
                if counts[c] < freq:
                    good = False
                    break
            if good:
                res += len(word)
        return res
    
    def countCharacters(self, words: List[str], chars: str) -> int:
        