class Solution:
    def reverseStr1(self, s: str, k: int) -> str:
        if not s or k <= 1:
            return s
        strList = [str(ch) for ch in s]
        if len(strList) <= k:
            self.reverseWord(strList, 0, len(strList) - 1)
        else:
            idx = 0
            while idx + k <= len(strList):
                self.reverseWord(strList, idx, idx + k - 1)
                idx += 2 * k
                if idx < len(strList) and idx + k > len(strList):
                    self.reverseWord(strList, idx, len(strList) - 1)
                    break

        return "".join(strList)

    def reverseWord(self, strList, l: int, r: int):
        while l < r:
            strList[l], strList[r] = strList[r], strList[l]
            l, r = l + 1, r - 1

    def reverseStr(self, s, k):
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a)

if __name__ == "__main__":
    s = "abcd"
    solution = Solution()
    ret = solution.reverseStr(s, 4)
    print(ret)