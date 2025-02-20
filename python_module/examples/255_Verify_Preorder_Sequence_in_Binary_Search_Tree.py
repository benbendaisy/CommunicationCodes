from typing import List


class Solution:
    def verifyPreorder1(self, preorder: List[int]) -> bool:
        stack, prev = [], None
        for node in preorder:
            # find the right node so that this node can become its right node
            # if less the first one, it means the node is still the left node
            while stack and node > stack[-1]:
                prev = stack.pop()

            # check if current node is bigger than its parent node as current node
            # should be the right node
            # if prev is None, it means that it is still left child
            if prev and node < prev:
                return False

            # push the node into stack
            stack.append(node)

        return True
    
    def verifyPreorder(self, preorder: List[int]) -> bool:
        @cache
        def helper(left: int, right: int, lower: int, upper: int) -> bool:
            if left > right:
                return True  # No elements to process

            root = preorder[left]
            if root <= lower or root >= upper:
                return False  # Value violates the BST condition

            idx = left + 1  # Start of the right subtree
            while idx <= right and preorder[idx] < root:
                idx += 1

            # Recursively check left and right subtrees
            return helper(left + 1, idx - 1, lower, root) and helper(idx, right, root, upper)
        
        return helper(0, len(preorder) - 1, float('-inf'), float('inf'))