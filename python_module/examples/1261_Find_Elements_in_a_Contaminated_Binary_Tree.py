# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.visited = set()
        self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.visited
    
    def dfs(self, cur_node, cur_value):
        if cur_node is None:
            return
        self.visited.add(cur_value)
        self.dfs(cur_node.left, cur_value * 2 + 1)
        self.dfs(cur_node.right, cur_value * 2 + 2)