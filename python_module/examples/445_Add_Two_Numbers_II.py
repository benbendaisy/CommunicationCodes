# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
        You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

        Example 1:

        Input: l1 = [7,2,4,3], l2 = [5,6,4]
        Output: [7,8,0,7]
        Example 2:

        Input: l1 = [2,4,3], l2 = [5,6,4]
        Output: [8,0,7]
        Example 3:

        Input: l1 = [0], l2 = [0]
        Output: [0]
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = 0, 0
        while l1:
            s1 = s1 * 10 + l1.val
            l1 = l1.next

        while l2:
            s2 = s2 * 10 + l2.val
            l2 = l2.next
        dummy_head = dummy = ListNode(0)
        for i in str(s1 + s2):
            dummy.next = ListNode(i)
            dummy = dummy.next
        return dummy_head.next