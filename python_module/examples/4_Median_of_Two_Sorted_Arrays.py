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
    
    def findMedianSortedArrays3(self, nums1: List[int], nums2: List[int]) -> float:
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
    
    def findMedianSortedArrays4(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)
        if n % 2 == 1:
            return float(merged[n // 2])
        else:
            mid1 = merged[n // 2 - 1]
            mid2 = merged[n // 2]
            return (mid1 + mid2) / 2.0
    
    def findMedianSortedArrays5(self, nums1: List[int], nums2: List[int]) -> float:
        merged = []
        i, j = 0, 0
        m, n = len(nums1), len(nums2)
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1
        while i < m:
            merged.append(nums1[i])
            i += 1
        while j < n:
            merged.append(nums2[j])
            j += 1
        
        mid = len(merged) // 2
        if len(merged) % 2 == 0:
            return (merged[mid - 1] + merged[mid]) / 2
        return merged[mid]

    def findMedianSortedArrays6(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        low, high = 0, m

        while low <= high:
            p_x = (low + high) // 2
            p_y = (m + n + 1) // 2 - p_x
            max_x = float('-inf') if p_x == 0 else nums1[p_x - 1]
            max_y = float('-inf') if p_y == 0 else nums2[p_y - 1]
            min_x = float('inf') if p_x == m else nums1[p_x]
            min_y = float('inf') if p_y == n else nums2[p_y]

            if max_x <= min_y and max_y <= min_x:
                if (m + n) % 2 == 0:
                    return (max(max_x, max_y) + min(min_x, min_y)) / 2
                else:
                    return max(max_x, max_y)
            elif max_x > min_y:
                high = p_x - 1
            else:
                low = p_x + 1

    def findMedianSortedArrays7(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2  # Midpoint for binary search

        left, right = 0, m
        while left <= right:
            partition1 = (left + right) // 2  # Partition in nums1
            partition2 = half - partition1  # Partition in nums2

            # Get left and right values for both partitions
            maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            minRight1 = float('inf') if partition1 == m else nums1[partition1]

            maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            minRight2 = float('inf') if partition2 == n else nums2[partition2]

            # Correct partition found
            if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
                if total % 2 == 0:
                    return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
                else:
                    return max(maxLeft1, maxLeft2)

            elif maxLeft1 > minRight2:
                right = partition1 - 1  # Move left in nums1
            else:
                left = partition1 + 1  # Move right in nums1

        raise ValueError("Input arrays are not sorted!")  # Should never happen
    
    def findMedianSortedArrays8(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return -1
        n1, n2 = len(nums1), len(nums2)
        n = n1 + n2
        def helper(k, n1_start, n1_end, n2_start, n2_end):
            if n1_start > n1_end:
                return nums2[k - n1_start]
            if n2_start > n2_end:
                return nums1[k - n2_start]
            
            n1_mid, n2_mid = (n1_start + n1_end) // 2, (n2_start + n2_end) // 2
            if n1_mid + n2_mid < k:
                if nums1[n1_mid] > nums2[n2_mid]:
                    return helper(k, n1_start, n1_end, n2_mid + 1, n2_end)
                else:
                    return helper(k, n1_mid + 1, n1_end, n2_start, n2_end)
            else:
                if nums1[n1_mid] > nums2[n2_mid]:
                    return helper(k, n1_start, n1_mid - 1, n2_start, n2_end)
                else:
                    return helper(k, n1_start, n1_end, n2_start, n2_end - 1)

        if n % 2:
            return helper(n // 2, 0, n1 - 1, 0, n2 - 1)

        return (helper(n // 2 - 1, 0, n1 - 1, 0, n2 - 1) + helper(n // 2, 0, n1 - 1, 0, n2 - 1)) / 2
    
    def findMedianSortedArrays9(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        half = (total + 1) // 2  # Ensure the left partition has one more element if total is odd
        
        # Binary search on the smaller array
        left, right = 0, n1
        while left <= right:
            partition1 = (left + right) // 2  # Partition for nums1
            partition2 = half - partition1   # Partition for nums2
            
            # Handle edge cases where partitions are out of bounds
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == n1 else nums1[partition1]
            
            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n2 else nums2[partition2]
            
            # Check if the partition is correct
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # If total number of elements is odd, return the max of the left partition
                if total % 2 == 1:
                    return max(max_left1, max_left2)
                # If even, return the average of the max of the left partition and the min of the right partition
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            elif max_left1 > min_right2:
                # Move the partition to the left in nums1
                right = partition1 - 1
            else:
                # Move the partition to the right in nums1
                left = partition1 + 1
        
        # If the input arrays are not sorted or other edge cases, return -1
        return -1
    
    def findMedianSortedArrays9(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return -1
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        half = (total + 1) // 2

        left, right = 0, n1
        while left <= right:
            p1 = (left + right) // 2
            p2 = half - p1

            max_left1 = float('-inf') if p1 == 0 else nums1[p1 - 1]
            min_right1 = float('inf') if p1 == n1 else nums1[p1]

            max_left2 = float('-inf') if p2 == 0 else nums2[p2 - 1]
            min_right2 = float('inf') if p2 == n2 else nums2[p2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if total % 2 == 1:
                    return max(max_left1, max_left2)
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            
            elif max_left1 > min_right2:
                right = p1 - 1
            else:
                left = p1 + 1
        return -1
    
    def findMedianSortedArrays10(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0.0
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        half = (total + 1) // 2
        left, right = 0, n1
        while left <= right:
            p1 = (left + right) // 2
            p2 = half - p1
            max_left1 = float('-inf') if p1 == 0 else nums1[p1 - 1]
            min_right1 = float('inf') if p1 == n1 else nums1[p1]

            max_left2 = float('-inf') if p2 == 0 else nums2[p2 - 1]
            min_right2 = float('inf') if p2 == n2 else nums2[p2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if total % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                right = p1 - 1
            else:
                left = p1 + 1
        return -1
    
    def findMedianSortedArrays11(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0.0
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        half = (total + 1) // 2
        left, right = 0, n1
        while left <= right:
            p1 = (left + right) // 2
            p2 = half - p1

            max_left1 = float('-inf') if p1 == 0 else nums1[p1 - 1]
            min_right1 = float('inf') if p1 == n1 else nums1[p1]

            max_left2 = float('-inf') if p2 == 0 else nums2[p2 - 1]
            min_right2 = float('inf') if p2 == n2 else nums2[p2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if total % 2 == 1:
                    return max(max_left1, max_left2)
                else:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            elif max_left1 < min_right2:
                left = p1 + 1
            else:
                right = p1 -1
        return -1
    
    def findMedianSortedArrays12(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        half = (total + 1) // 2
        left, right = 0, n1
        while left <= right:
            p1 = (left + right) // 2
            p2 = half - p1

            left_max1 = float('-inf') if p1 == 0 else nums1[p1 - 1]
            right_min1 = float('inf') if p1 == n1 else nums1[p1]

            left_max2 = float('-inf') if p2 == 0 else nums2[p2 - 1]
            right_min2 = float('inf') if p2 == n2 else nums2[p2]

            if left_max1 <= right_min2 and left_max2 <= right_min1:
                if total % 2 == 0:
                    return (max(left_max1, left_max2) + min(right_min1, right_min2)) / 2
                else:
                    return max(left_max1, left_max2)
            elif left_max1 < right_min2:
                left = p1 + 1
            else:
                right = p1 - 1
        return -1
    
    def findMedianSortedArrays13(self, nums1: List[int], nums2: List[int]) -> float:
        if not nums1 and not nums2:
            return 0.0
        
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        n1, n2 = len(nums1), len(nums2)
        total = n1 + n2
        half = (total + 1) // 2
        left, right = 0, n1
        while left <= right:
            p1 = (left + right) // 2
            p2 = half - p1
            left_max1 = float('-inf') if p1 == 0 else nums1[p1 - 1]
            left_min1 = float('inf') if p1 == n1 else nums1[p1]

            right_max2 = float('-inf') if p2 == 0 else nums2[p2 - 1]
            right_min2 = float('inf') if p2 == n2 else nums2[p2]

            if left_max1 <= right_min2 and right_max2 <= left_min1:
                if total % 2 == 1:
                    return max(left_max1, right_max2)
                else:
                    return (max(left_max1, right_max2) + min(left_min1, right_min2)) / 2
            elif left_max1 < right_max2:
                left = p1 + 1
            else:
                right = p1 - 1
        return -1
