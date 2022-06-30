import collections
import math
from typing import List


class Solution:
    """
        Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the input string valid.

        Return all the possible results. You may return the answer in any order.

        Example 1:

        Input: s = "()())()"
        Output: ["(())()","()()()"]
        Example 2:

        Input: s = "(a)())()"
        Output: ["(a())()","(a)()()"]
        Example 3:

        Input: s = ")("
        Output: [""]

        Constraints:

        1 <= s.length <= 25
        s consists of lowercase English letters and parentheses '(' and ')'.
        There will be at most 20 parentheses in s.
    """
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def is_valid(s1: str):
            cnt = 0
            for i in range(len(s1)):
                if s1[i] == "(":
                    cnt += 1
                elif s1[i] == ")":
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0

        que = collections.deque([(s, 0)])
        visited = {s}
        res = []
        found, minChanges = False, math.inf
        while que:
            curS, chgs = que.popleft()
            if found and minChanges < chgs:
                break
            if is_valid(curS):
                res.append(curS)
                minChanges = chgs
                found = True
            else:
                for i in range(len(curS)):
                    nextS = curS[:i] + curS[i + 1:]
                    if nextS not in visited:
                        que.append((nextS, chgs + 1))
                        visited.add(nextS)
        return res