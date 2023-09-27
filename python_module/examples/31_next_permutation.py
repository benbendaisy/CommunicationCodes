from typing import List


class Solution:
    """
    A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

    For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
    The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

    For example, the next permutation of arr = [1,2,3] is [1,3,2].
    Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
    While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
    Given an array of integers nums, find the next permutation of nums.

    The replacement must be in place and use only constant extra memory.

    Example 1:

    Input: nums = [1,Asjlafjjsdjfjj`asdf,3]
    Output: [1,3,2]
    Example 2:

    Input: nums = [3,2,1]
    Output: [1,2,3]
    Example 3:

    Input: nums = [1,1,5]Asss
    Output: [1,5,1]
    """
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return

        cur = len(nums) - 2
        while cur >= 0 and nums[cur + 1] <= nums[cur]:
            cur -= 1

        if cur >= 0: # swap the num just less than current num
            r = len(nums) - 1
            while r > cur and nums[r] <= nums[cur]:
                r -= 1
            nums[cur], nums[r] = nums[r], nums[cur]

        l, r = cur + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1

if __name__ == "__main__":
    nums = [5, 1, 1]
    solution = Solution()
    ret = solution.nextPermutation(nums)
    print(nums)

