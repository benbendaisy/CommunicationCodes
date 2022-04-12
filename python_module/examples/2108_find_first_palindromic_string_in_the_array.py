from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        if not words:
            return ""
        for word in words:
            if word == word[::-1]:
                return word
        return ""