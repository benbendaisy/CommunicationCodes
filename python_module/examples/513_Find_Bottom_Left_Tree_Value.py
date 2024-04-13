# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    Given the root of a binary tree, return the leftmost value in the last row of the tree.

    Example 1:

    Input: root = [2,1,3]
    Output: 1
    Example 2:

    Input: root = [1,2,3,4,null,5,6,null,null,7]
    Output: 7
    """
    def findBottomLeftValue1(self, root: Optional[TreeNode]) -> int:
        self.max_depth = -1
        self.left_value = 0
        def helper(node, depth):
            if not node:
                return
            if depth > self.max_depth:
                self.max_depth = depth
                self.left_value = node.val
            helper(node.left, depth + 1)
            helper(node.right, depth + 1)
            
        helper(root, 0)
        return self.left_value

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        que = deque()
        cur = root
        que.append(cur)
        while que:
            cur = que.popleft()
            if cur.right:
                que.append(cur.right)
            if cur.left:
                que.append(cur.left)
        return cur.val