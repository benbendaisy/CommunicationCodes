from typing import List


class Solution:
    """
        You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

        You are given an integer array nums representing the data status of this set after the error.

        Find the number that occurs twice and the number that is missing and return them in the form of an array.

        Example 1:

        Input: nums = [1,2,2,4]
        Output: [2,3]
        Example 2:

        Input: nums = [1,1]
        Output: [1,2]
    """
    def findErrorNums1(self, nums: List[int]) -> List[int]:
        if not nums or len(nums) < 2:
            return []
        nums.sort()
        dup = -1
        missing = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                dup = nums[i]
            elif nums[i] > nums[i - 1] + 1:
                missing = nums[i - 1] + 1
        missing = missing if nums[-1] == len(nums) else len(nums)
        return [dup, missing]
    
    def findErrorNums(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        num_dict = defaultdict(int)
        res = [0] * 2
        for num in nums:
            num_dict[num] += 1
        for i in range(1, n):
            if i not in num_dict:
                res[1] = i
            elif num_dict[i] == 2:
                res[0] = i

        if res[0] == 0:
            res[0] = n
        elif res[1] == 0:
            res[1] = n
            
        return res