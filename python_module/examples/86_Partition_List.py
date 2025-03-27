# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
        Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

        You should preserve the original relative order of the nodes in each of the two partitions.

        Example 1:

        Input: head = [1,4,3,2,5,2], x = 3
        Output: [1,2,2,4,3,5]
        Example 2:

        Input: head = [2,1], x = 2
        Output: [1,2]

        Constraints:

        The number of nodes in the list is in the range [0, 200].
        -100 <= Node.val <= 100
        -200 <= x <= 200
    """
    def partition1(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        less_head = less_tail = great_head = great_tail = None
        cur = head
        while cur:
            if cur.val < x:
                if not less_head or not less_tail:
                    less_head = less_tail = cur
                else:
                    less_tail.next = cur
                    less_tail = cur
            else:
                if not great_head or not great_tail:
                    great_head = great_tail = cur
                else:
                    great_tail.next = cur
                    great_tail = cur
            cur = cur.next
        if less_tail:
            less_tail.next = great_head
        if great_tail:
            great_tail.next = None
        return less_head if less_head else great_head
    
    def partition2(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before_head, after_head = ListNode(0), ListNode(0)
        before_tail, after_tail = before_head, after_head
        cur = head
        while cur:
            if cur.val < x:
                before_tail.next, before_tail = cur, cur
            else:
                after_tail.next, after_tail = cur, cur
            cur = cur.next
        after_tail.next = None
        before_tail.next = after_head.next
        return before_head.next
    
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_p, after_p = ListNode(), ListNode()
        p1, p2 = left_p, after_p
        cur = head
        while cur:
            if cur.val < x:
                p1.next = cur
                p1 = p1.next
            else:
                p2.next = cur
                p2 = p2.next
            cur = cur.next
        p2.next = None
        p1.next = after_p.next
        return left_p.next
