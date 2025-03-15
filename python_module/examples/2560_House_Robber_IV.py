class Solution:
    """
    There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.

    The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.

    You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.

    You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.

    Return the minimum capability of the robber out of all the possible ways to steal at least k houses.

    Example 1:

    Input: nums = [2,3,5,9], k = 2
    Output: 5
    Explanation: 
    There are three ways to rob at least 2 houses:
    - Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
    - Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
    - Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
    Therefore, we return min(5, 9, 9) = 5.
    Example 2:

    Input: nums = [2,7,9,3,1], k = 2
    Output: 2
    Explanation: There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.
    """
    def minCapability1(self, nums: List[int], k: int) -> int:
        """
        Memory Limit Exceeded
        """
        if not nums or len(nums) < k:
            return 0
        
        n = len(nums)
        @cache
        def helper(idx: int, h_num: int, max_num: int) -> int:
            if h_num >= k:
                return max_num
            if idx >= n:
                return float('inf')
            option1 = helper(idx + 1, h_num, max_num)

            value = max(nums[idx], max_num)
            option2 = helper(idx + 2, h_num + 1, value)

            return min(option1, option2)
        
        return helper(0, 0, float('-inf'))
    
    def minCapability1(self, nums: List[int], k: int) -> int:
        # Binary search approach is more efficient for this problem
        left, right = min(nums), max(nums)
        
        def feasible(capability):
            # Check if we can rob at least k houses with given capability
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= capability:
                    count += 1
                    i += 2  # Skip adjacent house
                else:
                    i += 1
            return count >= k
        
        # Binary search for minimum capability
        while left < right:
            mid = (left + right) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        
        return left
    
    def minCapability(self, nums: List[int], k: int) -> int:
        if not nums and len(nums) < k:
            return 0
        left, right = min(nums), max(nums)
        def feasible(capability):
            cnt, i = 0, 0
            while i < len(nums):
                if nums[i] <= capability:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= k
        
        while left < right:
            mid = (left + right) // 2
            if feasible(mid):
                right = mid
            else:
                left = mid + 1
        return left