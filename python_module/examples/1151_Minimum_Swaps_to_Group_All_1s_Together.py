class Solution:
    """
    Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

    Example 1:

    Input: data = [1,0,1,0,1]
    Output: 1
    Explanation: There are 3 ways to group all 1's together:
    [1,1,1,0,0] using 1 swap.
    [0,1,1,1,0] using 2 swaps.
    [0,0,1,1,1] using 1 swap.
    The minimum is 1.
    Example 2:

    Input: data = [0,0,0,1,0]
    Output: 0
    Explanation: Since there is only one 1 in the array, no swaps are needed.
    Example 3:

    Input: data = [1,0,1,0,1,0,0,1,1,0,1]
    Output: 3
    Explanation: One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
    """
    def minSwaps1(self, data: List[int]) -> int:
        ones_count = sum(data)  # Total number of 1s in the array
        if ones_count == 0:
            return 0
        
        max_ones_in_window = 0
        current_ones = 0
        left = 0
        
        # Sliding window approach
        for right in range(len(data)):
            current_ones += data[right]
            
            if right - left + 1 > ones_count:
                current_ones -= data[left]
                left += 1
            
            max_ones_in_window = max(max_ones_in_window, current_ones)
        
        return ones_count - max_ones_in_window
    
    def minSwaps2(self, data: List[int]) -> int:
        ones_cnt = sum(data)
        if ones_cnt < 2:
            return 0
        
        max_ones_in_window, cur_ones = 0, 0
        left, n = 0, len(data)
        for right in range(n):
            cur_ones += data[right]
            if right - left + 1 > ones_cnt:
                cur_ones -= data[left]
                left += 1
            max_ones_in_window = max(max_ones_in_window, cur_ones)
        return ones_cnt - max_ones_in_window
    
    def minSwaps3(self, data: List[int]) -> int:
        ones_cnt = sum(data)
        if ones_cnt < 2:
            return 0
        
        max_ones_in_window, cur_ones = 0, 0
        n, left = len(data), 0
        for right in range(n):
            cur_ones += data[right]
            if right - left + 1 > ones_cnt:
                cur_ones -= data[left]
                left += 1
            max_ones_in_window = max(max_ones_in_window, cur_ones)
        return ones_cnt - max_ones_in_window