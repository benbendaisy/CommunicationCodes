# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists1(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    cur.next = ListNode(list1.val)
                    list1 = list1.next
                else:
                    cur.next = ListNode(list2.val)
                    list2 = list2.next
            elif list1:
                cur.next = ListNode(list1.val)
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val)
                list2 = list2.next
            cur = cur.next
        return dummy.next
    
    def mergeTwoLists2(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = prev = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        
        if list1:
            prev.next = list1
        
        if list2:
            prev.next = list2
        return dummy.next
    
    def mergeTwoLists3(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode()
        while list1 or list2:
            if list1 and list2:
                if list1.val < list2.val:
                    cur.next = list1
                    list1 = list1.next
                else:
                    cur.next = list2
                    list2 = list2.next
            elif list1:
                cur.next = list1
                list1 = list1.next
            elif list2:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        return dummy.next