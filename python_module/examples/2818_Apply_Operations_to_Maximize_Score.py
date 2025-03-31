class Solution:
    """
    You are given an array nums of n positive integers and an integer k.

    Initially, you start with a score of 1. You have to maximize your score by applying the following operation at most k times:

    Choose any non-empty subarray nums[l, ..., r] that you haven't chosen previously.
    Choose an element x of nums[l, ..., r] with the highest prime score. If multiple such elements exist, choose the one with the smallest index.
    Multiply your score by x.
    Here, nums[l, ..., r] denotes the subarray of nums starting at index l and ending at the index r, both ends being inclusive.

    The prime score of an integer x is equal to the number of distinct prime factors of x. For example, the prime score of 300 is 3 since 300 = 2 * 2 * 3 * 5 * 5.

    Return the maximum possible score after applying at most k operations.

    Since the answer may be large, return it modulo 109 + 7.

    Example 1:

    Input: nums = [8,3,9,3,8], k = 2
    Output: 81
    Explanation: To get a score of 81, we can apply the following operations:
    - Choose subarray nums[2, ..., 2]. nums[2] is the only element in this subarray. Hence, we multiply the score by nums[2]. The score becomes 1 * 9 = 9.
    - Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 1, but nums[2] has the smaller index. Hence, we multiply the score by nums[2]. The score becomes 9 * 9 = 81.
    It can be proven that 81 is the highest score one can obtain.
    Example 2:

    Input: nums = [19,12,14,6,10,18], k = 3
    Output: 4788
    Explanation: To get a score of 4788, we can apply the following operations: 
    - Choose subarray nums[0, ..., 0]. nums[0] is the only element in this subarray. Hence, we multiply the score by nums[0]. The score becomes 1 * 19 = 19.
    - Choose subarray nums[5, ..., 5]. nums[5] is the only element in this subarray. Hence, we multiply the score by nums[5]. The score becomes 19 * 18 = 342.
    - Choose subarray nums[2, ..., 3]. Both nums[2] and nums[3] have a prime score of 2, but nums[2] has the smaller index. Hence, we multipy the score by nums[2]. The score becomes 342 * 14 = 4788.
    It can be proven that 4788 is the highest score one can obtain.
    """
    def maximumScore(self, nums: List[int], k: int) -> int:
        mod = 10 ** 9 + 7
        def primeFactors(n):
            i = 2
            ans = set()
            while i * i <= n:
                while n % i == 0:
                    ans.add(i)
                    n //= i
                i += 1
            if n > 1:
                ans.add(n)
            return len(ans)
        
        arr = [(i, primeFactors(x), x) for i, x in enumerate(nums)]
        n = len(nums)

        left = [-1] * n
        right = [n] * n
        stk = []
        for i, f, x in arr:
            while stk and stk[-1][0] < f:
                stk.pop()
            if stk:
                left[i] = stk[-1][1]
            stk.append((f, i))

        stk = []
        for i, f, x in arr[::-1]:
            while stk and stk[-1][0] <= f:
                stk.pop()
            if stk:
                right[i] = stk[-1][1]
            stk.append((f, i))

        arr.sort(key=lambda x: -x[2])
        ans = 1
        for i, f, x in arr:
            l, r = left[i], right[i]
            cnt = (i - l) * (r - i)
            if cnt <= k:
                ans = ans * pow(x, cnt, mod) % mod
                k -= cnt
            else:
                ans = ans * pow(x, k, mod) % mod
                break
        return ans

    def maximumScore(self, nums: List[int], k: int) -> int:
        """
        Time Limit Exceeded
        """
        MOD = 10**9 + 7
    
        # Helper function to calculate the prime score of a number
        def prime_score(n):
            score = 0
            i = 2
            seen = set()  # To track distinct prime factors
            
            while i * i <= n:
                while n % i == 0:
                    if i not in seen:
                        score += 1
                        seen.add(i)
                    n //= i
                i += 1
                
            # If n is a prime number greater than sqrt(n)
            if n > 1 and n not in seen:
                score += 1
                
            return score
        
        # Calculate prime scores for all elements
        n = len(nums)
        prime_scores = [prime_score(num) for num in nums]
        
        # Generate all possible subarrays and their best elements
        subarrays = []
        
        for l in range(n):
            for r in range(l, n):
                # Find element with highest prime score in this subarray
                max_ps = -1
                max_idx = -1
                
                for i in range(l, r + 1):
                    if prime_scores[i] > max_ps or (prime_scores[i] == max_ps and i < max_idx):
                        max_ps = prime_scores[i]
                        max_idx = i
                
                # Add to priority queue with negative value for max heap behavior
                subarrays.append((-nums[max_idx], l, r))
        
        # Sort by value (highest first)
        heapq.heapify(subarrays)
        
        score = 1
        used_subarrays = set()
        operations = 0
        
        while operations < k and subarrays:
            neg_val, l, r = heapq.heappop(subarrays)
            subarray_key = (l, r)
            
            if subarray_key not in used_subarrays:
                value = -neg_val  # Convert back to positive
                score = (score * value) % MOD
                used_subarrays.add(subarray_key)
                operations += 1
        
        return score