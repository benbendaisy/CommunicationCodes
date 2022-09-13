import collections
from typing import List


class Solution:
    """
        You are given an integer array nums that is sorted in non-decreasing order.

        Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

        Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
        All subsequences have a length of 3 or more.
        Return true if you can split nums according to the above conditions, or false otherwise.

        A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

        Example 1:

        Input: nums = [1,2,3,3,4,5]
        Output: true
        Explanation: nums can be split into the following subsequences:
        [1,2,3,3,4,5] --> 1, 2, 3
        [1,2,3,3,4,5] --> 3, 4, 5
        Example 2:

        Input: nums = [1,2,3,3,4,4,5,5]
        Output: true
        Explanation: nums can be split into the following subsequences:
        [1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
        [1,2,3,3,4,4,5,5] --> 3, 4, 5
        Example 3:

        Input: nums = [1,2,3,4,4,5]
        Output: false
        Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.

        Constraints:

        1 <= nums.length <= 104
        -1000 <= nums[i] <= 1000
        nums is sorted in non-decreasing order.
    """
    def isPossible1(self, nums: List[int]) -> bool:
        counter = collections.Counter(nums)
        for i in sorted(counter.keys()):
            while counter[i] > 0:
                last = 0
                j = i
                k = 0
                while counter[j] >= last:
                    last = counter[j]
                    counter[j] -= 1
                    j += 1
                    k += 1
                if k < 3:
                    return False
        return True

    def isPossible(self, nums: List[int]) -> bool:
        left = collections.Counter(nums) # key: number, val: how many of key are left unchecked
        seq = collections.defaultdict(int) # key: ending number, val: how many seqs
        for num in nums:
            if not left[num]: # the number is already in seqs, we don't need to check again
                continue
            left[num] -= 1
            if seq[num - 1] > 0:  # If there is sequence before the number, we add the number to the seq
                seq[num - 1] -= 1
                seq[num] += 1
            elif left[num + 1] and left[num + 2]: # If we create a new seq using the number
                left[num + 1] -= 1
                left[num + 2] -= 1
                seq[num + 2] += 1
            else:  #  If there aren't two numbers behind to let us create new seq, return False
                return False
        return True