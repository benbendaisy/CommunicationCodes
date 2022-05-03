class Solution:
    def isStrobogrammatic1(self, num: str) -> bool:
        if not num:
            return True

        l, r  = 0, len(num) - 1
        while l < r:
            if (num[l] == "9" and num[r] == "6") or (num[l] == "6" and num[r] == "9") or (num[l] == "8" and num[r] == "8") or (num[l] == "1" and num[r] == "1") or (num[l] == "0" and num[r] == "0"):
                l, r = l + 1, r - 1
            else:
                return False
        if l == r:
            return num[l] == "1" or num[l] == "8" or num[l] == "0"
        return True

    def isStrobogrammatic(self, num: str) -> bool:
        charMap = {"0":"0", "1":"1", "8":"8", "6":"9", "9":"6"}

        rotateString = []
        for ch in num[::-1]:
            if ch in charMap:
                rotateString.append(charMap[ch])
            else:
                return False
        return "".join(rotateString) == num

if __name__ == "__main__":
    num = "69"
    solution = Solution()
    ret = solution.isStrobogrammatic(num)
    print(ret)