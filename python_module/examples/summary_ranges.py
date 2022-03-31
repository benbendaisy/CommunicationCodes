from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        prev = 0
        res = []
        for i in range(len(nums)):
            if i + 1 < len(nums) and nums[i] + 1 == nums[i + 1]:
                continue
            elif prev == i:
                res.append(str(nums[prev]))
            else:
                res.append(str(nums[prev]) + "->" + str(nums[i]))
            prev = i + 1

        return res


    def summaryRanges1(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
        prev, cur = 0, 0
        res = []
        for i in range(1, len(nums)):
            if nums[cur] + 1 != nums[i]:
                if prev == cur:
                    res.append(str(nums[prev]))
                else:
                    res.append(str(nums[prev]) + "->" + str(nums[cur]))
                prev = i
            cur = i

        if prev == cur:
            res.append(str(nums[prev]))
        else:
            res.append(str(nums[prev]) + "->" + str(nums[cur]))
        return res