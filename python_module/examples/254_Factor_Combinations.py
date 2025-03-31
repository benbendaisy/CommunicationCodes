import math
from typing import List


class Solution:
    def getFactors1(self, n: int) -> List[List[int]]:
        def getFactor(n, factors, idx):
            if n == 1:
                if len(factors) > 1:
                    res.append(factors)
                return
            for i in range(idx, n + 1):
                if n % i == 0:
                    factors.append(i)
                    getFactor(n // i, factors, i)
                    factors.pop()
        res = []
        getFactor(n, [], 2)
        return res

    def getFactors2(self, n: int) -> List[List[int]]:
        def getFactor(n, factors, idx):
            if len(factors) > 0:
                res.append(factors + [n])
            sqrt = int(math.sqrt(n))
            for i in range(idx, sqrt + 1):
                if n % i == 0:
                    getFactor(n // i, factors + [i], i)
        res = []
        getFactor(n, [], 2)
        return res

    def getFactors3(self, n: int) -> List[List[int]]:
        if n <= 2:
            return []

        res = []
        def getFactor(t=n, factors=[], idx=2):
            if len(factors) > 0:
                res.append(factors + [t])
            for i in range(idx, int(math.sqrt(t)) + 1):
                if t % i == 0:
                    getFactor(t // i, factors + [i], i)
        getFactor(n, [], 2)
        return res
    
    def getFactors4(self, n: int) -> List[List[int]]:
        def backtrack(start, target, path, result):
            if target == 1:
                if len(path) > 1:
                    result.append(path.copy())
                return
            
            for i in range(start, target + 1):
                if i > target:
                    break
                if target % i == 0:
                    path.append(i)
                    backtrack(i, target // i, path, result)
                    path.pop()
        
        result = []
        backtrack(2, n, [], result)
        return result
    
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        def helper(start: int, target: int, path: list):
            if target == 1:
                if len(path) > 1:
                    path.sort()
                    res.append(path)
                return
            
            for i in range(start, target + 1):
                if target % i == 0:
                    helper(i, target // i, path + [i])
        helper(2, n, [])
        return res


if __name__ == "__main__":
    n = 7511016
    solution = Solution()
    ret = solution.getFactors(n)
    print(ret)