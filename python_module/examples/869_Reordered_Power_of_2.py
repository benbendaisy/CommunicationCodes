from typing import List


class Solution:
    def reorderedPowerOf1(self, n: int) -> bool:
        def validatePowerOf2(k):
            while k % 2 == 0 and k > 1:
                k /= 2
            return k == 1

        def permutation(strList: List):
            def getAllPermutations(idx: int):
                if idx == len(strList) and strList[0] != '0':
                    res.append(int("".join(strList)))
                for i in range(idx, len(strList)):
                    strList[idx], strList[i] = strList[i], strList[idx]
                    getAllPermutations(idx + 1)
                    strList[idx], strList[i] = strList[i], strList[idx]
            getAllPermutations(0)

        res = []
        strList = list(str(n))
        permutation(strList)
        for num in res:
            if validatePowerOf2(num):
                return True

        return False

    def reorderedPowerOf2(self, n: int) -> bool:
        def validatePowerOf2(k):
            while k % 2 == 0 and k > 1:
                k /= 2
            return k == 1

        def permutation(strList: List):
            def getAllPermutations(idx: int):
                if idx == len(strList) and strList[0] != '0':
                    res.append(int("".join(strList)))
                for i in range(idx, len(strList)):
                    strList[idx], strList[i] = strList[i], strList[idx]
                    getAllPermutations(idx + 1)
                    strList[idx], strList[i] = strList[i], strList[idx]
            getAllPermutations(0)
        res = []
        strList = list(str(n))
        permutation(strList)
        return any(validatePowerOf2(cand) for cand in res)

if __name__ == "__main__":
    n = 453686452
    solution = Solution()
    ret = solution.reorderedPowerOf2(n)
    print(ret)