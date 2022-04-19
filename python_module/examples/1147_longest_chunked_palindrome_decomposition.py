class Solution:
    def longestDecomposition(self, text: str) -> int:
        i, j = 0, len(text) - 1
        cnt = 0
        left = right = ""
        while i < j:
            left += text[i]
            right = text[j] + right
            if left == right:
                left = ""
                right = ""
                cnt += 2
            i, j = i + 1, j - 1
        if (left != "" and left == right) or i == j:
            cnt += 1
        return cnt