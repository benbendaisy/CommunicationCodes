class Solution:
    """
    
    """
    def numOfSubarrays1(self, arr: List[int]) -> int:
        m = len(arr)
        cnt = 0
        for i in range(m):
            for j in range(i + 1, m + 1):
                if sum(arr[i : j]) % 2 == 1:
                    cnt += 1
        return cnt
    
    def numOfSubarrays(self, arr: List[int]) -> int:
        """
        Count the number of subarrays with an odd sum.
        
        Args:
            arr: List of integers
            
        Returns:
            Number of subarrays with odd sum, modulo 10^9 + 7
        """
        MOD = 10**9 + 7
        n = len(arr)
        
        # We'll use prefix sums to solve this efficiently
        # odd_count will track the number of prefix sums that are odd
        # even_count will track the number of prefix sums that are even
        odd_count = 0
        even_count = 1  # Start with 1 because empty prefix has sum 0 (even)
        
        result = 0
        prefix_sum = 0
        
        for num in arr:
            # Update the current prefix sum
            prefix_sum += num
            
            # If the current prefix sum is odd
            if prefix_sum % 2 == 1:
                # Add the count of even prefixes seen so far
                # (odd - even = odd)
                result = (result + even_count) % MOD
                odd_count += 1
            else:
                # Add the count of odd prefixes seen so far
                # (even - odd = odd)
                result = (result + odd_count) % MOD
                even_count += 1
        
        return result