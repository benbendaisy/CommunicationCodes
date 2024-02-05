from typing import List


class Solution:
    """
    You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i], return true if and only if all the given nodes form exactly one valid binary tree.

    If node i has no left child then leftChild[i] will equal -1, similarly for the right child.

    Note that the nodes have no values and that we only use the node numbers in this problem.

    Example 1:

    Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1]
    Output: true
    Example 2:

    Input: n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1]
    Output: false
    Example 3:

    Input: n = 2, leftChild = [1,0], rightChild = [-1,-1]
    Output: false
    """
    def validateBinaryTreeNodes1(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def find_root():
            children = set(leftChild) | set(rightChild)
            for i in range(n):
                if i not in children:
                    return i
            return -1
        root = find_root()
        visited = {root}
        stack = [root]
        while stack:
            node = stack.pop()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in visited:
                        return False
                    stack.append(child)
                    visited.add(child)
        return len(visited) == n
    
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        def find_root():
            children = set(leftChild) | set(rightChild)
            for i in range(n):
                if i not in children:
                    return i
            return -1
        root = find_root()
        visited = {root}
        que = deque([root])
        while que:
            node = que.popleft()
            for child in [leftChild[node], rightChild[node]]:
                if child != -1:
                    if child in visited:
                        return False
                    que.append(child)
                    visited.add(child)
        return len(visited) == n