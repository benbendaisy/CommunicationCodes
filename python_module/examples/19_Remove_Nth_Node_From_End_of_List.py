# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd1(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode()
        prev.next = head

        first = head
        second = prev
        cnt = 0
        while first and cnt < n:
            first = first.next
            cnt += 1

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return prev.next
    
    def removeNthFromEnd2(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = ListNode()
        prev.next = head
        cnt = 0
        fast = head
        slow = prev
        while fast and cnt < n:
            fast = fast.next
            cnt += 1
        
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return prev.next
    
    def removeNthFromEnd3(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy  # `slow` follows `fast` n steps behind

        # Move `fast` ahead by `n + 1` steps
        for _ in range(n + 1):
            fast = fast.next

        # Move both `fast` and `slow` until `fast` reaches the end
        while fast:
            fast = fast.next
            slow = slow.next

        # Remove the Nth node
        slow.next = slow.next.next

        return dummy.next  # Return new head

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head
        fast = slow = dummy
        for _ in range(n + 1):
            if not fast: # this should never happen
                return head
            fast = fast.next
        
        while fast:
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        return dummy.next