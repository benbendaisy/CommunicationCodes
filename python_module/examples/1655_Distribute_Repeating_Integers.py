class Solution:
    """
    You are given an array of n integers, nums, where there are at most 50 unique values in the array. You are also given an array of m customer order quantities, quantity, where quantity[i] is the amount of integers the ith customer ordered. Determine if it is possible to distribute nums such that:

    The ith customer gets exactly quantity[i] integers,
    The integers the ith customer gets are all equal, and
    Every customer is satisfied.
    Return true if it is possible to distribute nums according to the above conditions.

    Example 1:

    Input: nums = [1,2,3,4], quantity = [2]
    Output: false
    Explanation: The 0th customer cannot be given two different integers.
    Example 2:

    Input: nums = [1,2,3,3], quantity = [2]
    Output: true
    Explanation: The 0th customer is given [3,3]. The integers [1,2] are not used.
    Example 3:

    Input: nums = [1,1,2,2], quantity = [2,2]
    Output: true
    Explanation: The 0th customer is given [1,1], and the 1st customer is given [2,2].
    """
    def canDistribute1(self, nums: List[int], quantity: List[int]) -> bool:
        # Count frequency of each unique number
        freq = list(Counter(nums).values())

        # Sort quantity in descending order for better pruning
        quantity.sort(reverse=True)
        
        @cache
        def helper(i: int, freq: tuple) -> bool:
            """
            Recursively tries to distribute quantities[i:] among available frequencies.
            """
            if i == len(quantity):  # All quantities are satisfied
                return True
            
            for j in range(len(freq)):
                if freq[j] >= quantity[i]:  # If this frequency can satisfy the current quantity
                    new_freq = list(freq)
                    new_freq[j] -= quantity[i]
                    if helper(i + 1, tuple(new_freq)):  # Recur for the next quantity
                        return True
            
            return False  # If no valid distribution is found
        
        return helper(0, tuple(freq))
    
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        freq = list(Counter(nums).values())

        quantity.sort(reverse=True)
        @cache
        def helper(idx: int, freq: tuple) -> bool:
            if idx == len(quantity):
                return True
            
            for i in range(len(freq)):
                if freq[i] >= quantity[idx]:
                    new_freq = list(freq)
                    new_freq[i] -= quantity[idx]
                    if helper(idx + 1, tuple(new_freq)):
                        return True
            return False
        
        return helper(0, tuple(freq))
