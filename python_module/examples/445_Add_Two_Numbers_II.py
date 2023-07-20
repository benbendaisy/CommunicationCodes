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
    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
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
    
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1, stack2 = [], []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        carry, res = 0, None
        while stack1 or stack2:
            sum_val = carry
            if stack1:
                sum_val += stack1.pop()
            if stack2:
                sum_val += stack2.pop()
            node = ListNode(sum_val % 10)
            node.next = res
            res = node
            carry = sum_val // 10
        return res
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list(head: ListNode):
            prev, cur = None, head
            while cur:
                t = cur.next
                cur.next = prev
                prev = cur
                cur = t
            return prev
        def add_helper(ll1: ListNode, ll2: ListNode):
            dummy = ListNode(0)
            tail = dummy
            carry = 0
            while ll1 or ll2 or carry:
                digit1 = ll1.val if ll1 else 0
                digit2 = ll2.val if ll2 else 0
                t = digit1 + digit2 + carry
                node = ListNode(t % 10)
                tail.next = node
                tail = node
                ll1 = ll1.next if ll1 else None
                ll2 = ll2.next if ll2 else None
                carry = t // 10
            return dummy.next

        l1 = reverse_list(l1)
        l2 = reverse_list(l2)
        return reverse_list(add_helper(l1, l2)) 
