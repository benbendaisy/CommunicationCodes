import math
from typing import List


class Solution:
    def find132pattern1(self, nums: List[int]) -> bool:
        if not nums:
            return False

        def find132patterns(idx: int, cnt: int, firstIdx: int):
            n = len(nums)
            if idx + cnt >= n:
                return False

            for i in range(idx + 1, n):
                if cnt == 2 and nums[i] > nums[idx] and find132patterns(i, cnt - 1, idx):
                    return True
                elif cnt == 1 and nums[i] < nums[idx] and nums[firstIdx] < nums[i]:
                    return True

            if cnt == 2 and find132patterns(idx + 1, cnt, firstIdx):
                return True

            return False

        return find132patterns(0, 2, 0)

    def find132pattern2(self, nums: List[int]) -> bool:
        if not nums:
            return False

        n = len(nums)
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if nums[i] < nums[j] > nums[k] and nums[i] < nums[k]:
                        return True
        return False

    def find132pattern3(self, nums: List[int]) -> bool:
        if not nums:
            return False

        minx = math.inf
        n = len(nums)
        for j in range(n - 1):
            minx = min(minx, nums[j])
            for k in range(j + 1, n):
                if minx < nums[k] < nums[j]:
                    return True
        return False

    def find132pattern(self, nums: List[int]) -> bool:
        if not nums:
            return False
        
        n = len(nums)
        min_array = [math.inf] * n
        min_array[0] = nums[0]
        for i in range(1, n):
            min_array[i] = min(min_array[i - 1], nums[i])
        
        stack = []
        for j in range(n - 1, -1, -1):
            if min_array[j] == nums[j]:
                continue
            while stack and stack[-1] <= min_array[j]:
                stack.pop()
            if stack and nums[j] > stack[-1]:
                return True
            stack.append(nums[j])
        return False

if __name__ == "__main__":
    nums = [1,1,0,1,0,1,0,1,0,0,0,1,1,1,1,0,0,0,0,1,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,1,0,0,1,0,0,1,1,1,1,1,1,1,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1,1,0,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,0,1,0,0,0,0,0,1,0,1,0,0,1,1,0,0,0,1,1,0,0,0,0,0,1,0,1,1,1,0,0,0,1,1,1,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,1,0,0,1,0,0,1,0,0,0,0,1,0,1,0,0,1,1,1,1,0,0,0,0,0,1,1,1,0,1,1,0,1,1,0,1,0,0,0,1,0,0,1,0,0,1,0,1,1,0,0,0,0,1,1,0,0,1,0,0,1,1,1,1,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1,0,1,1,1,1,1,1,0,1,1,1,0,1,1,1,1,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1,1,0,0,0,1,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,1,1,0,0,1,0,1,0,0,1,0,1,1,1,1,1,0,1,1,0,1,1,0,1,0,1,1,0,0,0,1,0,1,0,0,1,0,0,0,0,0,1,1,0,1,0,0,1,0,0,0,1,0,0,1,1,1,1,0,1,0,1,0,1,0,0,1,0,1,1,1,1,1,1,1,0,1,0,0,1,0,0,1,1,1,1,0,0,1,0,0,0,0,1,1,0,1,1,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,0,1,1,1,0,1,0,1,1,1,0,0,0,0,1,1,0,0,0,1,0,1,1,1,0,1,1,0,0,0,0,0,1,0,0,1,0,0,1,1,0,1,0,1,0,1,0,1,1,0,1,0,0,1,1,1,1,0,1,0,1,1,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,1,1,1,0,0,1,1,0,0,0,1,0,1,0,0,1,1,0,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,1,0,1,0,1,0,1,1,0,0,0,0,1,0,1,0,1,0,1,1,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,1,1,0,0,0,0,1,1,0,1,0,1,0,0,0,0,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,0,1,1,1,1,1,0,0,1,1,1,1,0,0,0,1,1,0,1,0,1,1,0,1,0,1,0,0,1,0,0,1,1,0,1,0,0,0,0,0,1,1,0,0,0,1,1,1,0,0,1,0,1,1,0,0,1,1,1,0,1,1,1,0,0,0,0,0,0,0,1,0,0,1,1,0,1,1,0,0,0,1,0,1,0,0,0,1,1,1,1,1,0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,1,1,0,1,1,1,0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,1,0,1,0,1,0,0,0,1,0,1,1,1,1,1,0,0,1,0,1,1,1,1,0,0,0,0,1,0,0,1,1,0,0,1,0,1,1,1,0,0,0,0,0,1,1,0,1,1,0,0,0,0,1,1,1,1,0,1,1,1,1,1,0,1,1,0,0,0,1,0,1,0,0,0,1,0,0,1,1,0,0,0,1,1,0,0,1,1,1,0,1,0,0,1,1,1,1,0,0,1,1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,1,0,1,0,1,0,0,1,1,1,1,1,1,0,1,0,1,1,0,1,0,0,0,0,0,0,0,1,1,1,0,1,1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,0,1,1,0,0,1,1,1,0,0,1,0,0,0,0,1,0,1,0,1,1,1,0,1,0,1,0,1,0,0,0,1,0,1,1,0,1,1,0,1,1,1,1,0,0,1,1,0,0,0,0,1,1,1,1,0,1,1,0,0,1,1,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,1,0,1,0,1,0,1,0,0,0,0,0,1,1,1,0,1,1,1,1,0,0,1,0,0,1,0,1,1,1,1,1,1,1,0,0,0,1,1,0,0,1,1,1,1,1,0,0,0,0,0,1,0,1,0,0,0,1,1,1,1,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0,1,0,0,1,0,0,1,0,0,0,1,0,0,1,1,1,0,0,1,1,0,1,1,1,1,1,0,1,0,1,1,0,0,0,1,1,0,1,1,0,0,1,0,0,1,0,1,0,1,1,0,1,0,1,1,0,0,1,0,1,0,1,1,0,0,1,0,1,0,1,0,0,0,1,1,1,1,0,1,0,0,1,0,1,0,1,0,1,0,0,0,0,0,0,0,0,0,1,0,1,1,1,0,1,1,0,0,1,0,0,0,0,0,0,1,1,0,0,1,1,0,1,1,0,0,1,0,0,0,0,1,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,1,1,0,0,1,0,0,0,1,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,0,0,1,1,0,0,0,0,0,1,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0,1,0,1,1,1,0,1,0,1,1,0,0,1,1,0,1,0,1,1,1,1,1,0,1,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1,0,1,1,0,1,0,0,0,1,1,1,1,1,0,1,0,0,1,0,1,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1,1,0,1,1,0,0,1,0,0,0,1,0,1,1,1,0,0,0,1,0,1,0,0,1,1,1,0,0,1,0,1,1,1,1,0,0,1,0,0,0,1,0,1,0,0,1,1,0,0,1,0,1,0,0,1,0,1,0,1,1,0,0,0,0,1,1,0,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,0,1,0,0,1,0,1,1,0,1,1,0,0,1,0,0,1,0,1,0,0,1,1,0,0,0,1,0,0,0,0,0,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,0,1,1,0,1,1,0,0,1,0,1,0,0,1,0,0,0,1,0,1,0,1,0,1,1,1,0,0,1,1,0,0,0,0,0,0,1,0,1,1,0,1,1,1,1,0,0,0,0,1,1,1,0,1,1,1,0,0,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,0,1,0,1,1,0,0,0,1,1,1,1,1,0,0,0,1,1,0,1,0,0,0,0,0,1,1,0,0,1,1,1,1,0,0,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,0,0,1,1,0,1,0,0,1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,0,1,0,1,1,0,1,1,1,0,1,0,1,1,0,0,1,0,0,1,0,0,0,1,1,0,1,0,0,1,1,0,1,1,0,0,1,1,0,1,1,1,0,0,0,0,1,0,0,0,0,1,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0,1,0,1,0,0,0,0,1,0,1,1,0,1,0,0,0,0,1,0,1,0,1,1,1,0,0,1,1,1,0,0,0,1,0,0,1,0,1,0,0,1,0,1,1,0,1,0,0,1,0,0,0,1,0,0,1,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1,1,0,0,0,0,0,1,0,1,1,1,1,1,1,1,1,0,1,0,0,0,1,0,0,0,0,0,1,1,0,1,0,1,1,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,0,0,0,0,0,1,1,1,0,1,1,0,1,0,0,1,1,1,0,1,0,1,1,1,0,0,1,0,0,0,0,1,0,1,1,1,1,0,1,0,0,0,1,0,0,0,0,1,1,1,1,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,1,1,1,1,1,0,1,1,0,0,1,1,0,0,0,0,1,0,1,0,1,1,1,1,1,0,1,0,1,0,1,0,0,0,1,1,1,0,1,0,1,0,1,0,0,1,0,0,1,1,0,0,1,1,1,0,0,0,1,0,0,0,1,1,1,0,1,1,0,0,0,1,0,0]
    solution = Solution()
    ret = solution.find132pattern(nums)
    print(ret)

