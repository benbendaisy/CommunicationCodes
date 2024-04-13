# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    You are given the head of a singly linked-list. The list can be represented as:

    L0 → L1 → … → Ln - 1 → Ln
    Reorder the list to be on the following form:

    L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
    You may not modify the values in the list's nodes. Only nodes themselves may be changed.

    Example 1:

    Input: head = [1,2,3,4]
    Output: [1,4,2,3]
    Example 2:

    Input: head = [1,2,3,4,5]
    Output: [1,5,2,4,3]
    """
    def reorderList1(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        cur = slow.next
        slow.next = None
        prev = None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        head2 = prev
        head1 = head
        while head1 and head2:
            head1.next, head1 = head2, head1.next
            head2.next, head2 = head1, head2.next
        
        def reorderList(self, head: Optional[ListNode]) -> None:
            """
                Do not return anything, modify head in-place instead.
            """
            if not head:
                return
            # find the middle of linked list [Problem 876]
            # in 1->2->3->4->5->6 find 4
            slow = fast = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            # reverse the second part of the list [Problem 206]
            # convert 1->2->3->4->5->6 into 1->2->3->4 and 6->5->4
            # reverse the second half in-place
            prev, cur = None, slow
            while cur:
                cur.next, prev, cur = prev, cur, cur.next
            # merge two sorted linked lists [Problem 21]
            # merge 1->2->3->4 and 6->5->4 into 1->6->2->5->3->4
            first, second = head, prev
            while second.next:
                first.next, first = second, first.next
                second.next, second = first, second.next