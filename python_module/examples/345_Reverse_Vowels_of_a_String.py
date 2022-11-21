class Solution:
    """
        Given a string s, reverse only all the vowels in the string and return it.

        The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

        Example 1:

        Input: s = "hello"
        Output: "holle"
        Example 2:

        Input: s = "leetcode"
        Output: "leotcede"
    """
    def reverseVowels1(self, s: str) -> str:
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        m = len(s)
        l, r = 0, len(s) - 1

        sList = list(s)
        while l <= r:
            while l <= r and sList[l] not in vowels:
                l += 1
            while l <= r and sList[r] not in vowels:
                r -= 1
            if 0 <= l < m and 0 <= r < m and sList[l] in vowels and sList[r] in vowels:
                sList[l], sList[r] = sList[r], sList[l]
            l += 1
            r -= 1
        return "".join(sList)

    def reverseVowels(self, s: str) -> str:
        if not s:
            return s
        vowels = set(list("aeiouAEIOU"))
        sList = list(s)
        vowel_idxes = [i for i, v in enumerate(s) if v in vowels]
        l, r = 0, len(vowel_idxes) - 1
        while l < r:
            sList[vowel_idxes[l]], sList[vowel_idxes[r]] = sList[vowel_idxes[r]], sList[vowel_idxes[l]]
            l, r = l + 1, r - 1
        return "".join(sList)
