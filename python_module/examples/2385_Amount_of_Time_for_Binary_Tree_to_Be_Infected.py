# Definition for a binary tree node.
from pyparsing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    """
    You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.

    Each minute, a node becomes infected if:

    The node is currently uninfected.
    The node is adjacent to an infected node.
    Return the number of minutes needed for the entire tree to be infected.

    Example 1:

    Input: root = [1,5,3,null,4,10,6,9,2], start = 3
    Output: 4
    Explanation: The following nodes are infected during:
    - Minute 0: Node 3
    - Minute 1: Nodes 1, 10 and 6
    - Minute 2: Node 5
    - Minute 3: Node 4
    - Minute 4: Nodes 9 and 2
    It takes 4 minutes for the whole tree to be infected so we return 4.
    Example 2:


    Input: root = [1], start = 1
    Output: 0
    Explanation: At minute 0, the only node in the tree is infected so we return 0.
    """
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        tree_map = defaultdict(set)
        def convert(current, parent):
            if not current:
                return
            adj_set = tree_map[current.val]
            if parent != 0:
                adj_set.add(parent)
            if current.left:
                adj_set.add(current.left.val)
            if current.right:
                adj_set.add(current.right.val)
            convert(current.left, current.val)
            convert(current.right, current.val)
        convert(root, 0)
        que = deque([start])
        visited = {start}
        minute = 0
        while que:
            level_size = len(que)
            while level_size > 0:
                current = que.popleft()
                for num in tree_map[current]:
                    if num not in visited:
                        visited.add(num)
                        que.append(num)
                level_size -= 1
            minute += 1
        return minute - 1