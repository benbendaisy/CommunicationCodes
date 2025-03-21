class Solution:
    """
    Given an array nums of size n, return the majority element.

    The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

    Example 1:

    Input: nums = [3,2,3]
    Output: 3
    Example 2:

    Input: nums = [2,2,1,1,1,2,2]
    Output: 2
    """
    def majorityElement1(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)

    def majorityElement2(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]
    
    def majorityElement3(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return max(freq.keys(), key=freq.get)
    
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        nums.sort()
        n = len(nums)
        return nums[n // 2]