from typing import List


class Solution:
    """
        You are given an array of positive integers nums and want to erase a subarray containing unique elements. The score you get by erasing the subarray is equal to the sum of its elements.

        Return the maximum score you can get by erasing exactly one subarray.

        An array b is called to be a subarray of a if it forms a contiguous subsequence of a, that is, if it is equal to a[l],a[l+1],...,a[r] for some (l,r).

        Example 1:

        Input: nums = [4,2,4,5,6]
        Output: 17
        Explanation: The optimal subarray here is [2,4,5,6].
        Example 2:

        Input: nums = [5,2,1,2,5,2,1,2,5]
        Output: 8
        Explanation: The optimal subarray here is [5,2,1] or [1,2,5].

        Constraints:

        1 <= nums.length <= 105
        1 <= nums[i] <= 104
    """
    def maximumUniqueSubarray1(self, nums: List[int]) -> int:
        l = r = 0
        n = len(nums)
        hashSet = set()
        maxSum = 0
        while r < n:
            while r < n and nums[r] not in hashSet:
                hashSet.add(nums[r])
                r += 1
            maxSum = max(maxSum, sum(nums[l:r]))
            while r < n and l < r and nums[l] != nums[r]:
                hashSet.remove(nums[l])
                l += 1

            l += 1 # handle the nums[l] == nums[r]
            if r < n and nums[r] in hashSet: # remove the duplicate from hashSet
                hashSet.remove(nums[r])
        return maxSum

    def maximumUniqueSubarray2(self, nums: List[int]) -> int:
        l = r = 0
        n = len(nums)
        sums = [0] * n
        sums[0] = nums[0]
        hashSet = set()
        for i in range(1, n):
            sums[i] = sums[i - 1] + nums[i]

        maxSum = 0
        while r < n:
            while r < n and nums[r] not in hashSet:
                hashSet.add(nums[r])
                r += 1
            maxSum = max(maxSum, sums[r - 1] - sums[l - 1]) if l != 0 else sums[r - 1]
            while r < n and l < r and nums[l] != nums[r]:
                hashSet.remove(nums[l])
                l += 1
            l += 1
            if r < n and nums[r] in hashSet:
                hashSet.remove(nums[r])
        return maxSum

    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        curSum = 0
        n = len(nums)
        idx = 0
        hashSet = set()
        maxSum = 0
        for i in range(n):
            while nums[i] in hashSet:
                hashSet.remove(nums[idx])
                curSum -= nums[idx]
                idx += 1
            curSum += nums[i]
            hashSet.add(nums[i])
            maxSum = max(maxSum, curSum)
        return maxSum

if __name__ == "__main__":
    nums = [4,2,4,5,6]
    solution = Solution()
    ret = solution.maximumUniqueSubarray(nums)
    print(ret)
