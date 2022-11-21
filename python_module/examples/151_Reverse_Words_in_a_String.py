class Solution:
    def reverseWords(self, s: str) -> str:
        if not s or len(s) < 2:
            return s

        char_list = s.split()
        l, r = 0, len(char_list) - 1
        while l < r:
            char_list[l], char_list[r] = char_list[r], char_list[l]
            l, r = l + 1, r - 1
        return " ".join(char_list)
