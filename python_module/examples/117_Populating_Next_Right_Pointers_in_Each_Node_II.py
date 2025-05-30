"""
# Definition for a Node.
Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Example 1:


Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
Example 2:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 6000].
-100 <= Node.val <= 100
"""
import collections


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect1(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = collections.deque([root])

        while queue:
            length = len(queue)
            for i in range(length):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i < length - 1:
                    node.next = queue[0]

        return root
    
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        dep_dict = defaultdict(list)
        def helper(node: 'Node', dep: int):
            if not node:
                return
            
            dep_dict[dep].append(node)
            helper(node.left, dep + 1)
            helper(node.right, dep + 1)

        helper(root, 0)
        for row in dep_dict.values():
            for i in range(len(row) - 1):
                row[i].next = row[i + 1]
        return root


