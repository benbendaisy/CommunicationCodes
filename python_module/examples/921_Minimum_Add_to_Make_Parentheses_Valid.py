class Solution:
    """
    A parentheses string is valid if and only if:

    It is the empty string,
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.
    You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

    For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
    Return the minimum number of moves required to make s valid.

    Example 1:

    Input: s = "())"
    Output: 1
    Example 2:

    Input: s = "((("
    Output: 3
    """
    def minAddToMakeValid(self, s: str) -> int:
        if not s:
            return 0
        
        stack = []
        cnt = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
            elif ch == ")":
                if not stack:
                    cnt += 1
                else:
                    stack.pop()
        return cnt + len(stack)