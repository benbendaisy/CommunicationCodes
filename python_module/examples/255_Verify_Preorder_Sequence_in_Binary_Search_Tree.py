from typing import List


class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
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