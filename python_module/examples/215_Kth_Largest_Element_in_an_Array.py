import heapq
from random import random
from typing import List


class Solution:
    """
        Given an integer array nums and an integer k, return the kth largest element in the array.

        Note that it is the kth largest element in the sorted order, not the kth distinct element.

        Example 1:

        Input: nums = [3,2,1,5,6,4], k = 2
        Output: 5
        Example 2:

        Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
        Output: 4

        Constraints:

        1 <= k <= nums.length <= 104
        -104 <= nums[i] <= 104
    """
    def findKthLargest1(self, nums: List[int], k: int) -> int:
        if len(nums) < k:
            return -1

        nums.sort(reverse=True)
        return nums[k - 1]

    def findKthLargest2(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(nums, k)[-1]

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        quick select
        :param nums: the given a list of nums
        :param k: the kth largest num
        :return: the kth largest num
        """
        def partition1(l: int, r: int):
            pivot, ptr = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr += 1
            nums[ptr], nums[r] = nums[r], nums[ptr]
            return ptr

        def partition(l: int, r: int):
            pivot, ptr = random.randint(l, r), l
            nums[pivot], nums[r] = nums[r], nums[pivot]
            for i in range(l, r):
                if nums[i] <= nums[r]:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr += 1
            nums[ptr], nums[r] = nums[r], nums[ptr]
            return ptr

        def quickSelect(l: int, r: int, m: int):
            if l == r:
                return nums[l]
            idx = partition(l, r)
            if idx == m:
                return nums[idx]
            elif idx > m:
                return quickSelect(l, idx - 1, m)

            return quickSelect(idx + 1, r, m)


        return quickSelect(0, len(nums) - 1, len(nums) - k)

if __name__ == "__main__":
    nums = [1,2,1,3,2,5]
    solution = Solution()
    ret = solution.findKthLargest(nums, 2)
    print(ret)

