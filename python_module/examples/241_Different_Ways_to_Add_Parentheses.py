class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ops = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }
        
        def dfs(exp):
            ans = []
            for i, c in enumerate(exp):
                if c in ops:
                    left, op, right = exp[:i], exp[i], exp[i + 1:]
                    for l in dfs(left):
                        for r in dfs(right):
                            ans.append(ops[op](l, r))
            if exp.isnumeric():
                ans.append(int(exp))
            return ans
        return dfs(expression)