class Solution:
    def reverseVowels(self, s: str) -> str:
        if not s:
            return s
        a = list(s)
        vowels = set(list("aeiouAEIOU"))
        idxs = [ i for i, c in enumerate(a) if c in vowels ]
        l, r = 0, len(idxs) - 1
        while l < r:
            a[idxs[l]], a[idxs[r]] = a[idxs[r]], a[idxs[l]]
            l, r = l + 1, r - 1
        return "".join(a)

if __name__ == "__main__":
    s = "aA"
    solution = Solution()
    ret = solution.reverseVowels(s)
    print(ret)