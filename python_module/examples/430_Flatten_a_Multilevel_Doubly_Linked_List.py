"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:
    """
        You are given a doubly linked list, which contains nodes that have a next pointer, a previous pointer, and an additional child pointer. This child pointer may or may not point to a separate doubly linked list, also containing these special nodes. These child lists may have one or more children of their own, and so on, to produce a multilevel data structure as shown in the example below.

        Given the head of the first level of the list, flatten the list so that all the nodes appear in a single-level, doubly linked list. Let curr be a node with a child list. The nodes in the child list should appear after curr and before curr.next in the flattened list.

        Return the head of the flattened list. The nodes in the list must have all of their child pointers set to null.

        Example 1:

        Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
        Output: [1,2,3,7,8,11,12,9,10,4,5,6]
        Explanation: The multilevel linked list in the input is shown.
        After flattening the multilevel linked list it becomes:

        Example 2:

        Input: head = [1,2,null,3]
        Output: [1,3,2]
        Explanation: The multilevel linked list in the input is shown.
        After flattening the multilevel linked list it becomes:

        Example 3:

        Input: head = []
        Output: []
        Explanation: There could be empty list in the input.
    """
    def flatten1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        def flat_dfs(prev_node: Node, cur_node: Node):
            if not cur_node:
                return prev_node
            prev_node.next = cur_node
            cur_node.prev = prev_node
            # the curr.next would be tempered in the recursive function
            t = cur_node.next
            tail = flat_dfs(cur_node, cur_node.child)
            cur_node.child = None
            return flat_dfs(tail, t)
        prev = Node(0, None, head, None)
        flat_dfs(prev, head)
        prev.next.prev = None
        return prev.next

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head

        pseudo_head = Node(0, None, head, None)
        prev = pseudo_head
        stack = []
        stack.append(head)
        while stack:
            cur = stack.pop()
            prev.next = cur
            cur.prev = prev
            if cur.next:
                stack.append(cur.nemxt)
            if cur.child:
                stack.append(cur.child)
                cur.child = None
            prev = cur
        pseudo_head.next.prev = None
        return pseudo_head.next

