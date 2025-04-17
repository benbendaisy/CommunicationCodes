import collections


class Solution:
    def longestValidParentheses1(self, s: str) -> int:
        if not s:
            return 0
        def isValid(str1: str) -> bool:
            stack = collections.deque()
            idx = 0
            while idx < len(str1):
                if str1[idx] == ")":
                    if stack:
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(str1[idx])
                idx += 1
            return not stack
        maxCnt = 0
        for i in range(len(s)):
            for j in range(i + 2, len(s) + 1, 2):
                if isValid(s[i : j]):
                    maxCnt = max(maxCnt, j - i)
        return maxCnt

    def longestValidParentheses2(self, s: str) -> int:
        if not s:
            return 0
        stack = []
        max_length = 0
        stack.append(-1)
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        return max_length

    def longestValidParentheses3(self, s: str) -> int:
        if not s or len(s) < 2:
            return 0
        stack = [-1]
        max_len = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i) # fix the issue when all valid parenthese pop
        return max_len


    def longestValidParentheses4(self, s: str) -> int:
        if not s:
            return 0
        stack, max_len = [-1], 0
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i)
        return max_len
    
    def longestValidParentheses5(self, s: str) -> int:
        if not s:
            return 0
        stack, max_len = [-1], 0
        for i, v in enumerate(s):
            if v == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_len = max(max_len, i - stack[-1])
                else:
                    stack.append(i) # mark as new start position
        return max_len


if __name__ == "__main__":
    s = "())()()(())((()(()()(((()))((((())((()(())()())(()" \
        "((((()))()(()))(())()(())(()(((((())((((((()())())" \
        "(()(()((())()))(()))))))()(()))((((())()()()))()()()" \
        "(((()(()())(()()(()(()()(((()))))))()()))())())((()" \
        "()))))))((()))(((()((())()(()()))((())))()()())))))))" \
        "()))))(()))))()))()))()((())))((()))(()))))))(((()))))))))" \
        "()(()()()(())((())()))()()(())))()()))(()())()))(((()())()))" \
        "((())((((()))(()(()(()()()(((())()(((((()))((()(((((())" \
        "(()()))((((((((()(()(()(()(())))(())(()())())(()((((()(())" \
        "((()(())))(())))()(((((()(()()(())))))))())(())(())(()()(((())))" \
        "((()))(((((()))))())))()((()))()))))())))))((())(((((()()))" \
        "((((())))(((()(()(())())(((()(()(()()()())))())()))((()((())" \
        "())()()()(((())(((((()((((((()((()())))((((())((()(((((((()(()" \
        "((()()()(()(()())(()(()()((((())))()(((()())))(()()))()(()()()" \
        "()(((((())(()))))((()))())))()((((((()))())))()(()))(())))((((()())" \
        "(((((()()())(((((())(()())(()))))()(()()))()))))))())))(((())(()(()()))" \
        "(()))()(((())))())((((()(((()))))))()(()(()))()()(()()))))))))((()))))))" \
        "(())((()((()))()))((((((()())))))(()((())((((()))))(()(()()()()(()))()()" \
        "(()(()))(()()(((((((()())(())(()())((())())()(()())((())()())())(()())))())))" \
        "(())())())(())((()())(((()()))()))()()))()(()(())((((((((())))()((())((()" \
        "((((((((((()))))(()(((((())(()(()())())))((())())))))()))(()((()()))((()((())" \
        "()()()((()(())())((())())(()()(((())))))())()()(()))()())(()(()((())))" \
        "((((()()(())))())(())(()(()(())())())(()()())()(())())))(()()(((())))" \
        "((()()(((())()()(()())((((()()(()())(()((((()(()()(()(()(((()((()())(()()))" \
        "(()((((()(((((()))))()()))(((()((((((()(()()()()())()))(()(())))))" \
        "((()(((()())())))(((()()))(()(()(((((((()()))(()(())))())()(())())(())" \
        "(()))(())(()))()()(()()())))))()))()((())(((()((((((((())()()))())))((()())("
    solution = Solution()
    ret = solution.longestValidParentheses(s)
    print(ret)

