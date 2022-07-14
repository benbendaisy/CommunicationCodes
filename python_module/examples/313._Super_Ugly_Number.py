import heapq
from typing import List


class Solution:
    """
        A super ugly number is a positive integer whose prime factors are in the array primes.

        Given an integer n and an array of integers primes, return the nth super ugly number.

        The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

        Example 1:

        Input: n = 12, primes = [2,7,13,19]
        Output: 32
        Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 super ugly numbers given primes = [2,7,13,19].
        Example 2:

        Input: n = 1, primes = [2,3,5]
        Output: 1
        Explanation: 1 has no prime factors, therefore all of its prime factors are in the array primes = [2,3,5].


        Constraints:

        1 <= n <= 105
        1 <= primes.length <= 100
        2 <= primes[i] <= 1000
        primes[i] is guaranteed to be a prime number.
        All the values of primes are unique and sorted in ascending order.
    """
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        uglyNumbers = [1]
        heap = []
        # initial the heap, (the next val to be evaluated,
        # the idx of the prime number, the last time used number position
        for idx, prime in enumerate(primes):
            heapq.heappush(heap, (prime, idx, 0))

        i = 0
        while i < n:

            # check the smallest number
            num, idx, pos = heapq.heappop(heap)

            # if can put in the result
            if num > uglyNumbers[-1]:
                uglyNumbers.append(num)
                i += 1
            # put the next candidate by putting the primes * the next can
            # use number in the dp list
            heapq.heappush(heap, (primes[idx] * uglyNumbers[pos + 1], idx, pos + 1))
        return uglyNumbers[n-1]

if __name__ == "__main__":
    n = 12
    primes = [2,7,13,19]
    solution = Solution()
    ret = solution.nthSuperUglyNumber(n, primes)
    print(ret)