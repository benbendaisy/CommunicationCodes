class Solution:
    def addDigits(self, num: int) -> int:
        numStr = str(num)

        while len(numStr) > 1:
            nums = [int(ch) for ch in numStr]
            numStr = str(sum(nums))

        return int(numStr)