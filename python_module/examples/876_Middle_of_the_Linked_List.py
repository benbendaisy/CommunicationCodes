# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
        Given the head of a singly linked list, return the middle node of the linked list.

        If there are two middle nodes, return the second middle node.

        Example 1:

        Input: head = [1,2,3,4,5]
        Output: [3,4,5]
        Explanation: The middle node of the list is node 3.
        Example 2:

        Input: head = [1,2,3,4,5,6]
        Output: [4,5,6]
        Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = runner = head
        while runner and runner.next:
            cur = cur.next
            runner = runner.next.next
        return cur