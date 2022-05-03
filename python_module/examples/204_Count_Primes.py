import math


class Solution:
    def __init__(self):
        self.primeStore = [2, 3, 5, 7, 11, 13, 17, 19]
    def checkPrime(self, n: int) -> bool:
        sqr = int(math.sqrt(n))
        for i in range(2, sqr + 1):
            if n % i == 0:
                return False
        return True

    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0

        if self.primeStore[-1] < n:
            for i in range(self.primeStore[-1] + 1, n + 1):
                if self.checkPrime(i):
                    self.primeStore.append(i)

        l = 0
        while l < len(self.primeStore) and self.primeStore[l] < n:
            l += 1
        return l

if __name__ == "__main__":
    n = 1500000
    solution = Solution()
    ret = solution.countPrimes(n)
    print(ret)



