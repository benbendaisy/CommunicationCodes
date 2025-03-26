class Solution:
    """
    You are given an integer array nums. We call a subset of nums good if its product can be represented as a product of one or more distinct prime numbers.

    For example, if nums = [1, 2, 3, 4]:
    [2, 3], [1, 2, 3], and [1, 3] are good subsets with products 6 = 2*3, 6 = 2*3, and 3 = 3 respectively.
    [1, 4] and [4] are not good subsets with products 4 = 2*2 and 4 = 2*2 respectively.
    Return the number of different good subsets in nums modulo 109 + 7.

    A subset of nums is any array that can be obtained by deleting some (possibly none or all) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

    Example 1:

    Input: nums = [1,2,3,4]
    Output: 6
    Explanation: The good subsets are:
    - [1,2]: product is 2, which is the product of distinct prime 2.
    - [1,2,3]: product is 6, which is the product of distinct primes 2 and 3.
    - [1,3]: product is 3, which is the product of distinct prime 3.
    - [2]: product is 2, which is the product of distinct prime 2.
    - [2,3]: product is 6, which is the product of distinct primes 2 and 3.
    - [3]: product is 3, which is the product of distinct prime 3.
    Example 2:

    Input: nums = [4,2,3,15]
    Output: 5
    Explanation: The good subsets are:
    - [2]: product is 2, which is the product of distinct prime 2.
    - [2,3]: product is 6, which is the product of distinct primes 2 and 3.
    - [2,15]: product is 30, which is the product of distinct primes 2, 3, and 5.
    - [3]: product is 3, which is the product of distinct prime 3.
    - [15]: product is 15, which is the product of distinct primes 3 and 5.
    """
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        res = set()
        nums.sort()
        def helper(start: int, path: tuple):
            if path:
                res.add(path)
            for i in range(start, n):
                helper(i + 1, path + (nums[i], ))

        helper(0, ())
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        @cache
        def product_of_distinct_primes(n):
            """Check if n is a product of distinct prime factors."""
            if n < 2:
                return False
            factors = set()
            for i in range(1, n):
                if n % i == 0 and is_prime(i):
                    # If we've seen this prime factor before, it's not a product of distinct primes
                    if i in factors:
                        return False
                    # Add prime factor to our set
                    factors.add(i)
                    # Divide n by the prime factor
                    n //= i
    
            # If we've factored n completely and all prime factors are distinct, return True
            return n == 1
            
        cnt = 0
        for tup in res:
            product = 1
            for num in tup:
                product *= num
            if product_of_distinct_primes(product):
                cnt += 1
        return cnt