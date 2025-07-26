class Solution:
    """
    A word is considered valid if:

    It contains a minimum of 3 characters.
    It contains only digits (0-9), and English letters (uppercase and lowercase).
    It includes at least one vowel.
    It includes at least one consonant.
    You are given a string word.

    Return true if word is valid, otherwise, return false.

    Notes:

    'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
    A consonant is an English letter that is not a vowel.

    Example 1:

    Input: word = "234Adas"

    Output: true

    Explanation:

    This word satisfies the conditions.

    Example 2:

    Input: word = "b3"

    Output: false

    Explanation:

    The length of this word is fewer than 3, and does not have a vowel.

    Example 3:

    Input: word = "a3$e"

    Output: false

    Explanation:

    This word contains a '$' character and does not have a consonant.
    """
    def isValid(self, word: str) -> bool:
        if not word or len(word) < 3:
            return False
        vowels = ["a", "e", "i", "o", "u"]
        consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
        is_vowel, is_consonant = False, False
        word = word.lower()
        for ch in word:
            if not (ch.isdigit() or ch.isalpha()):
                return False
            if ch in vowels and not (is_vowel):
                is_vowel = True
            if ch in consonants and not (is_consonant):
                is_consonant = True
        
        return is_vowel and is_consonant