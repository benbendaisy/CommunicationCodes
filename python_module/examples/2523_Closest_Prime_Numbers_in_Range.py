class Solution:
    """
    Given two positive integers left and right, find the two integers num1 and num2 such that:

    left <= num1 < num2 <= right .
    Both num1 and num2 are prime numbers.
    num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
    Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

    Example 1:

    Input: left = 10, right = 19
    Output: [11,13]
    Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
    The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
    Since 11 is smaller than 17, we return the first pair.
    Example 2:

    Input: left = 4, right = 6
    Output: [-1,-1]
    Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.
    """
    def closestPrimes1(self, left: int, right: int) -> List[int]:
        # Step 1: Use the Sieve of Eratosthenes to find all primes up to 'right'
        limit = right + 1
        is_prime = [True] * limit
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        for i in range(2, int(limit ** 0.5) + 1):
            if is_prime[i]:
                for multiple in range(i * i, limit, i):
                    is_prime[multiple] = False
        
        # Step 2: Collect primes in the range [left, right]
        primes = [i for i in range(left, right + 1) if is_prime[i]]

        # Step 3: Find the closest pair
        if len(primes) < 2:
            return [-1, -1]
            
        min_diff = float('inf')
        idx = -1
        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < min_diff:
                min_diff = primes[i] - primes[i - 1]
                idx = i
        return [-1, -1] if idx == -1 else [primes[idx - 1], primes[idx]]
    
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # Step 1: Use the Sieve of Eratosthenes to find all primes up to 'right'
        def is_prime(n: int) -> bool:
            if n < 2:
                return False
            if n in (2, 3):
                return True
            if n % 2 == 0 or n % 3 == 0:
                return False
            
            i = 5
            while i * i <= n:
                if n % i == 0 or n % (i + 2) == 0:
                    return False
                i += 6
            
            return True
        
        # Step 2: Collect primes in the range [left, right]
        primes = [i for i in range(left, right + 1) if is_prime(i)]

        # Step 3: Find the closest pair
        if len(primes) < 2:
            return [-1, -1]

        min_diff = float('inf')
        idx = -1
        for i in range(1, len(primes)):
            if primes[i] - primes[i - 1] < min_diff:
                min_diff = primes[i] - primes[i - 1]
                idx = i
        return [-1, -1] if idx == -1 else [primes[idx - 1], primes[idx]]

