class Solution:
    """
    You are given two arrays nums1 and nums2 consisting of positive integers.

    You have to replace all the 0's in both arrays with strictly positive integers such that the sum of elements of both arrays becomes equal.

    Return the minimum equal sum you can obtain, or -1 if it is impossible.

    Example 1:

    Input: nums1 = [3,2,0,1,0], nums2 = [6,5,0]
    Output: 12
    Explanation: We can replace 0's in the following way:
    - Replace the two 0's in nums1 with the values 2 and 4. The resulting array is nums1 = [3,2,2,1,4].
    - Replace the 0 in nums2 with the value 1. The resulting array is nums2 = [6,5,1].
    Both arrays have an equal sum of 12. It can be shown that it is the minimum sum we can obtain.
    Example 2:

    Input: nums1 = [2,0,2,0], nums2 = [1,4]
    Output: -1
    Explanation: It is impossible to make the sum of both arrays equal.
    """
    def minSum1(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return -1
        
        freq1, freq2 = Counter(nums1), Counter(nums2)
        sums1, sums2 = sum(nums1), sum(nums2)
        if (freq1[0] == 0 and sums1 < sums2 + freq2[0]) or (freq2[0] == 0 and sums2 < sums1 + freq1[0]):
            return -1
        
        return max(sums1 + freq1[0], sums2 + freq2[0])

    def minSum2(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return -1
        
        sum1 = sum2 = 0
        zero1 = zero2 = 0

        for num in nums1:
            sum1 += num
            if num == 0:
                sum1 += 1
                zero1 += 1
        
        for num in nums2:
            sum2 += num
            if num == 0:
                sum2 += 1
                zero2 += 1
        
        if (zero1 == 0 and sum1 < sum2) or (zero2 == 0 and sum2 < sum1): # can not add the num to nums
            return -1
        return max(sum1, sum2) # the diff can be added by 1
    
    def minSum3(self, nums1: List[int], nums2: List[int]) -> int:
        if not nums1 or not nums2:
            return -1
        
        zero1, zero2 = nums1.count(0), nums2.count(0)
        sum1, sum2 = sum(nums1) + zero1, sum(nums2) + zero2 # minimal change is to change zero to one
        
        if (zero1 == 0 and sum1 < sum2) or (zero2 == 0 and sum2 < sum1):
            return -1
        return max(sum1, sum2)
        