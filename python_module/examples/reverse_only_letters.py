class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        if not s:
            return s
        arr = [x for x in s if x.isalpha()]
        res = []
        for ch in s:
            if ch.isalpha():
                res.append(arr.pop())
            else:
                res.append(ch)
        return "".join(res)

    def reverseOnlyLetters1(self, s: str) -> str:
        if not s:
            return s

        idxes = [i for i, c in enumerate(s) if c.isalpha()]
        arr = [ch for ch in s]

        l, r = 0, len(idxes) - 1
        while l < r:
            arr[idxes[l]], arr[idxes[r]] = arr[idxes[r]], arr[idxes[l]]
            l, r = l + 1, r - 1

        return "".join(arr)

if __name__ == "__main__":
    s = [4,2,0,3,2,5]
    solution = Solution()
    ret = solution.reverseOnlyLetters(height)
    print(ret)