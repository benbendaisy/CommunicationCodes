class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if not word or not ch:
            return word

        words = [ch for ch in word]
        for i, c in enumerate(words):
            if c == ch:
                words[:i + 1] = words[:i + 1][::-1]
                break

        return "".join(words)