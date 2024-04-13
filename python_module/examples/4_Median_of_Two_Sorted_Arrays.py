from typing import List


class Solution:
    """
    Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).

    Example 1:

    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000
    Explanation: merged array = [1,2,3] and median is 2.
    Example 2:

    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000
    Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
    """
    def findMedianSortedArrays1(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the arrays into a single sorted array.
        merged = nums1 + nums2

        # Sort the merged array.
        merged.sort()

        # Calculate the total number of elements in the merged array.
        total = len(merged)

        if total % 2 == 1:
            # If the total number of elements is odd, return the middle element as the median.
            return float(merged[total // 2])
        else:
            # If the total number of elements is even, calculate the average of the two middle elements as the median.
            middle1 = merged[total // 2 - 1]
            middle2 = merged[total // 2]
            return (float(middle1) + float(middle2)) / 2.0
    
    def findMedianSortedArrays2(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        merged_array = [0] * (n1 + n2)
        idx1, idx2 = 0, 0
        for i in range(n1 + n2):
            if idx1 < n1 and (idx2 == n2 or nums1[idx1] < nums2[idx2]):
                merged_array[i] = nums1[idx1]
                idx1 += 1
            else:
                merged_array[i] = nums2[idx2]
                idx2 += 1
        if (n1 + n2) % 2 != 0:
            return merged_array[(n1 + n2) // 2]
        else:
            return (merged_array[(n1 + n2) // 2 - 1] + merged_array[(n1 + n2) // 2]) / 2.0
    
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        def helper(k, n1_start, n1_end, n2_start, n2_end):
            if n1_start > n1_end:
                return nums2[k - n1_start]
            if n2_start > n2_end:
                return nums1[k - n2_start]
            n1_idx, n2_idx = (n1_start + n1_end) // 2,  (n2_start + n2_end) // 2
            n1_val, n2_val = nums1[n1_idx], nums2[n2_idx]
            if n1_idx + n2_idx < k:
                if n1_val > n2_val:
                    return helper(k, n1_start, n1_end, n2_idx + 1, n2_end)
                else:
                    return helper(k, n1_idx + 1, n1_end, n2_start, n2_end)
            else:
                if n1_val > n2_val:
                    return helper(k, n1_start, n1_idx - 1, n2_start, n2_end)
                else:
                    return helper(k, n1_start, n1_end, n2_start, n2_idx - 1)
        if n % 2:
            return helper(n // 2, 0, n1 - 1, 0, n2 - 1)
        else:
            return (helper(n//2 - 1, 0, n1 - 1, 0, n2 - 1) + helper(n // 2, 0, n1 - 1, 0, n2 -1)) / 2
