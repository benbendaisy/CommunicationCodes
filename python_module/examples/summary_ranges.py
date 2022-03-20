class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
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