class Solution:
    """
        You are given two integer arrays nums1 and nums2 of length n.

        The XOR sum of the two integer arrays is (nums1[0] XOR nums2[0]) + (nums1[1] XOR nums2[1]) + ... + (nums1[n - 1] XOR nums2[n - 1]) (0-indexed).

        For example, the XOR sum of [1,2,3] and [3,2,1] is equal to (1 XOR 3) + (2 XOR 2) + (3 XOR 1) = 2 + 0 + 2 = 4.
        Rearrange the elements of nums2 such that the resulting XOR sum is minimized.

        Return the XOR sum after the rearrangement.

        Example 1:

        Input: nums1 = [1,2], nums2 = [2,3]
        Output: 2
        Explanation: Rearrange nums2 so that it becomes [3,2].
        The XOR sum is (1 XOR 3) + (2 XOR 2) = 2 + 0 = 2.
        Example 2:

        Input: nums1 = [1,0,3], nums2 = [5,3,4]
        Output: 8
        Explanation: Rearrange nums2 so that it becomes [5,4,3]. 
        The XOR sum is (1 XOR 5) + (0 XOR 4) + (3 XOR 3) = 4 + 4 + 0 = 8.
    """
    def minimumXORSum1(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
    
        # Recursive function with memoization
        @cache
        def helper(index, mask):
            # Base case: all elements in nums1 have been paired
            if index == n:
                return 0
            
            min_xor_sum = float('inf')
            # Try pairing the current element of nums1 with each available element in nums2
            for j in range(n):
                # Check if the j-th element of nums2 is available
                if (mask >> j) & 1 == 0:
                    # Calculate XOR value for this pairing
                    xor_value = nums1[index] ^ nums2[j]
                    # Mark j-th element as used in the mask
                    new_mask = mask | (1 << j)
                    # Recursive call for next index with updated mask
                    remaining_sum = helper(index + 1, new_mask)
                    
                    # Update minimum XOR sum
                    min_xor_sum = min(min_xor_sum, xor_value + remaining_sum)
            
            return min_xor_sum
        
        # Start with index 0 and empty mask (no elements used)
        return helper(0, 0)
    
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
    
        @cache
        def helper(idx, mask):
            if idx == n:
                return 0
            min_xor = float('inf')
            for i in range(n):
                if (mask >> i) & 1 == 0:
                    val = nums1[idx] ^ nums2[i]
                    new_mask = mask | (1 << i)
                    remaining_sum = helper(idx + 1, new_mask)
                    min_xor = min(min_xor, val + remaining_sum)
            return min_xor
        return helper(0, 0)