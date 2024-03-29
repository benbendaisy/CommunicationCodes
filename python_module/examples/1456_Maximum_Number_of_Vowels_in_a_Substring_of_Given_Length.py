class Solution:
    """
        Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

        Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

        Example 1:

        Input: s = "abciiidef", k = 3
        Output: 3
        Explanation: The substring "iii" contains 3 vowel letters.
        Example 2:

        Input: s = "aeiou", k = 2
        Output: 2
        Explanation: Any substring of length 2 contains 2 vowels.
        Example 3:

        Input: s = "leetcode", k = 3
        Output: 2
        Explanation: "lee", "eet" and "ode" contain 2 vowels.
    """
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(["a", "e", "i", "o", "u"])
        max_vowels = curr_vowels = 0
        for i, c in enumerate(s):
            if i >= k and s[i - k] in vowels:
                curr_vowels -= 1
            if c in vowels:
                curr_vowels += 1
            max_vowels = max(max_vowels, curr_vowels)
        return max_vowels