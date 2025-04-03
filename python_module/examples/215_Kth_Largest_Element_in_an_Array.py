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

    def findKthLargest3(self, nums: List[int], k: int) -> int:
        """
        quick select
        :param nums: the given a list of nums
        :param k: the kth largest num
        :return: the kth largest num
        """
        def partition1(l: int, r: int):
            pivot, ptr = nums[l], l  # `ptr` points to the partition index
            for i in range(l + 1, r + 1):  # Start from `l + 1` to avoid swapping pivot with itself
                if nums[i] < pivot:  # Strictly less than pivot to maintain order
                    ptr += 1
                    nums[i], nums[ptr] = nums[ptr], nums[i]  # Swap to move smaller elements left
            nums[l], nums[ptr] = nums[ptr], nums[l]  # Place pivot in correct position
            return ptr  # Return the pivot index

        def partition(l, r):
            pivot, ptr = random.randint(l, r), l
            nums[pivot], nums[r] = nums[r], nums[pivot]
            for i in range(l, r):
                if nums[i] <= nums[r]:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr += 1
            nums[ptr], nums[r] = nums[r], nums[ptr]
            return ptr
        
        def quick_select(l, r, m):
            if l == r:
                return nums[l]
            idx = partition(l, r)
            if idx == m:
                return nums[idx]
            elif idx > m:
                return quick_select(l, idx - 1, m)
            return quick_select(idx + 1, r, m)
        return quick_select(0, len(nums) - 1, len(nums) - k)
    
    def findKthLargest4(self, nums: List[int], k: int) -> int:
        min_heap = []
        for num in nums:
            if not min_heap or len(min_heap) < k:
                heapq.heappush(min_heap, num)
            elif num > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, num)
    
    def findKthLargest5(self, nums: List[int], k: int) -> int:
        def partition(l, r):
            pivot, ptr = random.randint(l, r), l
            nums[pivot], nums[r] = nums[r], nums[pivot]
            for i in range(l, r):
                if nums[i] <= nums[r]:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr += 1
            nums[ptr], nums[r] = nums[r], nums[ptr]
            return ptr
        def quick_select(l, r, m):
            if l == r:
                return nums[l]
            idx = partition(l, r)
            if idx == m:
                return nums[idx]
            elif idx > m:
                return quick_select(l, idx - 1, m)
            return quick_select(idx + 1, r, m)
        return quick_select(0, len(nums) - 1, len(nums) - k)
    
    def findKthLargest6(self, nums: List[int], k: int) -> int:
        def partition(l, r):
            pivot, ptr = random.randint(l, r), l
            nums[pivot], nums[r] = nums[r], nums[pivot]
            for i in range(l, r):
                if nums[i] <= nums[r]:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr += 1
            nums[ptr], nums[r] = nums[r], nums[ptr]
            return ptr
        
        def quick_select(left: int, right: int, t: int):
            if left == right:
                return nums[left]
            pos = partition(left, right)
            if pos == t:
                return nums[pos]
            elif pos < t:
                return quick_select(pos + 1, right, t)
            else:
                return quick_select(left, pos - 1, t)
        if not nums or len(nums) < k:
            return -1
        n = len(nums)
        return quick_select(0, n - 1, n - k)

    def findKthLargest7(self, nums: List[int], k: int) -> int:
        if not nums or len(nums) < k:
            return -1
        heap = []
        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            elif heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)
        return heap[0]
if __name__ == "__main__":
    nums = [1,2,1,3,2,5]
    solution = Solution()
    ret = solution.findKthLargest(nums, 2)
    print(ret)

