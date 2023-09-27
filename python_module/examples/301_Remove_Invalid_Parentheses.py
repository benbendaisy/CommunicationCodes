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
            for ch in s1:
                if ch == '(':
                    cnt += 1
                elif ch == ')':
                    cnt -= 1
                    if cnt < 0:
                        return False
            return cnt == 0
        que = deque([(s, 0)])
        visited = {s}
        found, min_changes = False, math.inf
        res = []
        while que:
            cur_string, cur_change = que.popleft()
            if found and min_changes < cur_change:
                break
            if is_valid(cur_string):
                res.append(cur_string)
                min_changes = cur_change
                found = True
            else:
                for i in range(len(cur_string)):
                    if cur_string[i] != '(' and cur_string[i] != ')':
                        continue
                    next_string = cur_string[:i] + cur_string[i + 1:]
                    if next_string not in visited:
                        que.append((next_string, cur_change + 1))
                        visited.add(next_string)
        return res