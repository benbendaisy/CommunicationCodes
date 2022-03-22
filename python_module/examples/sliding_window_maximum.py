from typing import List
from collections import deque
class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []
        elif k == 1:
            return nums
        deq = deque()
        def clean_que(i):
            if deq and deq[0] == i - k:
                deq.popleft()
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
        res = []
        max_idx = 0
        l = len(nums)
        for i in range(k):
            clean_que(i)
            deq.append(i)
            max_idx = i if nums[i] > nums[max_idx] else max_idx
        res.append(nums[max_idx])

        for i in range(k, l):
            clean_que(i)
            deq.append(i)
            res.append(nums[deq[0]])

        return res


    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []
        elif k == 1:
            return nums
        l = len(nums)

        left = [0] * l
        left[0] = nums[0]
        right = [0] * l
        right[l - 1] = nums[l - 1]

        for i in range(1, l):
            if i % k == 0:
                left[i] = nums[i]
            else:
                left[i] = max(left[i - 1], nums[i])

            j = l - i - 1
            if (j + 1) % k == 0:
                right[j] = nums[j]
            else:
                right[j] = max(right[j + 1], nums[j])

        return [max(left[i + k - 1], right[i]) for i in range(l - k + 1)]

    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        if not nums or k <= 0:
            return []
        elif k == 1:
            return nums
        return [max(nums[i: i + k]) for i in range(len(nums) - k + 1)]

if __name__ == "__main__":
    test = Solution()
    t = [1,3,-1,-3,5,3,6,7]
    print(test.maxSlidingWindow(t, 3))