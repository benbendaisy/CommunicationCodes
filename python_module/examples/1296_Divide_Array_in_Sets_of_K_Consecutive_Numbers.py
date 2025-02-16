class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        """
        Given an array of integers nums and a positive integer k, check whether it is possible to divide this array into sets of k consecutive numbers.

        Return true if it is possible. Otherwise, return false.

        Example 1:

        Input: nums = [1,2,3,3,4,4,5,6], k = 4
        Output: true
        Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].
        Example 2:

        Input: nums = [3,2,1,2,3,4,3,4,5,9,10,11], k = 3
        Output: true
        Explanation: Array can be divided into [1,2,3] , [2,3,4] , [3,4,5] and [9,10,11].
        Example 3:

        Input: nums = [1,2,3,4], k = 3
        Output: false
        Explanation: Each array should be divided in subarrays of size 3.
        """
        if not nums or k < 1:
            return False
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1
        for num in sorted(num_dict.keys()):
            cnt = num_dict[num]
            if cnt == 0:
                continue
            count = 0
            for i in range(k):
                num_dict[num + count] -= cnt
                if num_dict[num + count] < 0:
                    return False
                count += 1
        return True