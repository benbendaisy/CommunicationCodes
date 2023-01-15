from collections import defaultdict
from typing import List


class Solution:
    """
        You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

        Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.

        Example 1:

        Input: equations = ["a==b","b!=a"]
        Output: false
        Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
        There is no way to assign the variables to satisfy both equations.
        Example 2:

        Input: equations = ["b==a","a==b"]
        Output: true
        Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

        Constraints:

        1 <= equations.length <= 500
        equations[i].length == 4
        equations[i][0] is a lowercase letter.
        equations[i][1] is either '=' or '!'.
        equations[i][2] is '='.
        equations[i][3] is a lowercase letter.
    """
    def equationsPossible1(self, equations: List[str]) -> bool:
        graph = defaultdict(list)

        for eqn in equations:
            if eqn[1] == "=":
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')
                graph[x].append(y)
                graph[y].append(x)

        color = [-1] * 26

        # mark the color of node as c
        def dfs(node, c):
            if color[node] == -1:
                color[node] = c
                for nei in graph[node]:
                    dfs(nei, c)

        for i in range(26):
            if color[i] == -1:
                dfs(i, i)

        for eqn in equations:
            if eqn[1] == "!":
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')
                if color[x] == color[y]:
                    return False
        return True

    def equationsPossible(self, equations: List[str]) -> bool:
        root = list(range(26))
        def find(x):
            if x == root[x]:
                return x
            return find(root[x])

        def union(x, y):
            x, y = find(x), find(y)
            root[x] = y
            
        for eqn in equations:
            if eqn[1] == "=":
                x, y = ord(eqn[0])-ord('a'), ord(eqn[3])-ord('a')
                union(x, y)

        for eqn in equations:
            if eqn[1] == "!":
                x, y = ord(eqn[0])-ord('a'), ord(eqn[3])-ord('a')
                if find(x) == find(y):
                    return False
        return True

