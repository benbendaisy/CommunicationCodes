# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    Given the head of a singly linked list, reverse the list, and return the reversed list.

    Example 1:

    Input: head = [1,2,3,4,5]
    Output: [5,4,3,2,1]
    Example 2:

    Input: head = [1,2]
    Output: [2,1]
    Example 3:

    Input: head = []
    Output: []
    """
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head
        while cur:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
    
    def reverseList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev, cur = None, head
        while cur:
            t = cur.next
            cur.next = prev
            prev = cur
            cur = t
        return prev
    
    def reverseList3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        cur, prev = head, None
        while cur:
            t = cur.next
            cur.next = prev
            prev = cur
            cur = t
        return prev