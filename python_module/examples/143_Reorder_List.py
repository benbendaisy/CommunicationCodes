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
    def reorderList(self, head: Optional[ListNode]) -> None:
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