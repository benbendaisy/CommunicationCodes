import random
from typing import List


class Solution:
    """
        Given an array of integers nums, sort the array in ascending order and return it.

        You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

        Example 1:

        Input: nums = [5,2,3,1]
        Output: [1,2,3,5]
        Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
        Example 2:

        Input: nums = [5,1,1,2,0,0]
        Output: [0,0,1,1,2,5]
        Explanation: Note that the values of nums are not necessairly unique.
    """
    def sortArray1(self, nums: List[int]) -> List[int]:
        def partition(low, high):
            pivot = nums[high]
            i = low - 1
            for j in range(low, high):
                if nums[j] <= pivot:
                    i += 1
                    nums[i], nums[j] = nums[j], nums[i]
            nums[i + 1], nums[high] = nums[high], nums[i + 1]
            return i + 1

        def quick_sort(low, high):
            if low < high:
                pivot = partition(low, high)
                quick_sort(low, pivot - 1)
                quick_sort(pivot + 1, high)
        n = len(nums)
        quick_sort(0, n - 1)
        return nums

    def sortArray2(self, nums: List[int]) -> List[int]:
        def quick_sort(arr: List[int]):
            if len(arr) <= 1:
                return arr
            pivot = random.choice(arr)
            less, equal, greater = [], [], []
            for num in arr:
                if num == pivot:
                    equal.append(num)
                elif num < pivot:
                    less.append(num)
                else:
                    greater.append(num)
            return quick_sort(less) + equal + quick_sort(greater)
        return quick_sort(nums)

    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr: List[int]):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left, right)
        def merge(left, right):
            res = []
            idx, idy = 0, 0
            while idx < len(left) and idy < len(right):
                if left[idx] < right[idy]:
                    res.append(left[idx])
                    idx += 1
                else:
                    res.append(right[idy])
                    idy += 1
            res += left[idx:]
            res += right[idy:]
            return res
        return merge_sort(nums)

