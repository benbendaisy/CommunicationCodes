from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        prev = lower - 1
        for i in range(len(nums) + 1):
            cur = nums[i] if i < len(nums) else upper + 1
            if prev + 1 <= cur - 1:
                res.append(self.formatString(prev + 1, cur - 1))
        return res

    def formatString(self, low, upper):
        if low == upper:
            return str(low)
        return str(low) + "->" + str(upper)

if __name__ == "__main__":
    nums = [-1]
    solution = Solution()
    ret = solution.findMissingRanges(nums, -2, -1)
    print(ret)