import random
from typing import List


class Solution:
    """
        Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.

        In one move, you can increment or decrement an element of the array by 1.

        Test cases are designed so that the answer will fit in a 32-bit integer.

        Example 1:

        Input: nums = [1,2,3]
        Output: 2
        Explanation:
        Only two moves are needed (remember each move increments or decrements one element):
        [1,2,3]  =>  [2,2,3]  =>  [2,2,2]
        Example 2:

        Input: nums = [1,10,2,9]
        Output: 16

        Constraints:

        n == nums.length
        1 <= nums.length <= 105
        -109 <= nums[i] <= 109
    """
    def minMoves2(self, nums: List[int]) -> int:
        def partition(l: int, r: int):
            pivot = random.randint(l, r)
            nums[pivot], nums[r] = nums[r], nums[pivot]
            pivot, ptr = nums[r], l
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[ptr] = nums[ptr], nums[i]
                    ptr += 1
            nums[ptr], nums[r] = nums[r], nums[ptr]
            return ptr

        def findMedium():
            l, r = 0, len(nums) - 1
            m = len(nums) // 2
            while l < r:
                p = partition(l, r)
                if p == m:
                    return nums[p]
                elif p < m:
                    l = p + 1
                else:
                    r = p - 1
            return nums[l]
        medium = findMedium()
        cnt = 0
        for x in nums:
            cnt += abs(x - medium)
        return cnt

if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    ret = solution.minMoves2(nums)
    print(ret)