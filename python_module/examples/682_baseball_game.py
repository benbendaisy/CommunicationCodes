from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        if not ops:
            return 0

        arr = []
        for op in ops:
            if op == "+":
                a = int(arr[-1])
                b = int(arr[-2])
                arr.append(a + b)
            elif op == "D":
                it = int(arr[-1])
                arr.append(it * 2)
            elif op == "C":
                arr.pop()
            else:
                arr.append(op)
        res = [int(x) for x in arr]
        return sum(res)

if __name__ == "__main__":
    ops = ["5","2","C","D","+"]
    solution = Solution()
    ret = solution.calPoints(ops)
    print(ret)