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
    
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
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
