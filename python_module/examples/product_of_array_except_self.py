from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
            if not nums:
                return -1
            zero_set = [x for x in range(len(nums)) if nums[x] == 0]
            if len(zero_set) > 1:
                return [0 for x in nums]
            temp = 1
            for item in nums:
                if item != 0:
                    temp *= item
            if len(zero_set) == 1:
                return [temp if x == 0 else 0 for x in nums]
            return [temp//x for x in nums]

if __name__ == "__main__":
    test = Solution()
    t = [1, 2, 3, 4]
    print(test.productExceptSelf(t))