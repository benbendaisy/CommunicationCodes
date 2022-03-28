from typing import List


class Solution:
    def diffWaysToCompute1(self, expression: str) -> List[int]:
        from collections import defaultdict, deque
        cache = defaultdict(list)
        ops = {x for x in "+-*/"}
        def calculateExp(a, b, op) -> int:
            x, y = int(a), int(b)
            if op == '+':
                return x + y
            elif op == '-':
                return x - y
            elif op ==  '*':
                return x * y
            else:
                return x / y

        def dfs(exp: str):
            if exp in cache: return cache[exp]

            if exp.isnumeric():
                cache[exp].append(int(exp))

            for i, c in enumerate(exp):
                if not c in ops:
                    continue

                left, op, right = exp[:i], exp[i], exp[i + 1:]
                for l in dfs(left):
                    for r in dfs(right):
                        cache[exp].append(calculateExp(l, r, op))
            return cache[exp]

        dfs(expression)
        return cache[expression]

    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }
        def dfs(exp):
            ans = []
            for i, c in enumerate(exp):
                if c in "+-*/":
                    l, op, r = exp[:i], exp[i], exp[i + 1:]
                    for left in dfs(l):
                        for right in dfs(r):
                            ans.append(ops[exp](left, right))
            # if the exp is a num that is either the left or right most
            if exp.isnumeric():
                ans.append(int(exp))
            return ans

        return dfs(expression)
