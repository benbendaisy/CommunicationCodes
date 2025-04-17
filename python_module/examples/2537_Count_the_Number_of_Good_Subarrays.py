class Solution:
    """
    Given an integer array nums and an integer k, return the number of good subarrays of nums.

    A subarray arr is good if there are at least k pairs of indices (i, j) such that i < j and arr[i] == arr[j].

    A subarray is a contiguous non-empty sequence of elements within an array.

    Example 1:

    Input: nums = [1,1,1,1,1], k = 10
    Output: 1
    Explanation: The only good subarray is the array nums itself.
    Example 2:

    Input: nums = [3,1,4,3,2,2,4], k = 2
    Output: 4
    Explanation: There are 4 different good subarrays:
    - [3,1,4,3,2,2] that has 2 pairs.
    - [3,1,4,3,2,2,4] that has 3 pairs.
    - [1,4,3,2,2,4] that has 2 pairs.
    - [4,3,2,2,4] that has 2 pairs.
    """
    def countGood1(self, nums: List[int], k: int) -> int:
        """
        Memory Limited Exceeded
        """
        n = len(nums)

        def count_pairs(freq: dict) -> int:
            pairs = 0
            for count in freq.values():
                if count >= 2:
                    pairs += (count * (count - 1)) // 2
            return pairs

        @cache
        def helper(start: int, end: int, freq: tuple) -> int:
            if end >= n:
                return 0

            new_freq = list(freq)
            val = nums[end]
            new_freq[val] += 1
            total_pairs = count_pairs(Counter({i: new_freq[i] for i in range(len(new_freq)) if new_freq[i] > 0}))
            
            cnt = 1 if total_pairs >= k else 0
            cnt += helper(start, end + 1, tuple(new_freq))
            return cnt

        total = 0
        for start in range(n):
            freq = [0] * 100001  # assuming nums[i] ≤ 10^5
            total += helper(start, start, tuple(freq))
        return total
    
    def countGood2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = 0
        freq = defaultdict(int)
        pairs = 0
        ans = 0

        for right in range(n):
            num = nums[right]
            pairs += freq[num]
            freq[num] += 1

            while pairs >= k:
                ans += n - right  # all subarrays [left...right], [left+1...right], ..., [right...right] are good
                freq[nums[left]] -= 1
                pairs -= freq[nums[left]]  # remove the number of pairs that included nums[left]
                left += 1

        return ans