# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers1(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_node(node: ListNode):
            if not node:
                return node
            prev = None
            while node:
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt
            return prev
        l1_reverse = l1
        l2_reverse = l2
        carrier = 0
        prev = node = ListNode()
        while l1_reverse and l2_reverse:
            sum_value = carrier + l1_reverse.val + l2_reverse.val
            new_node = ListNode(sum_value % 10)
            node.next = new_node
            node = node.next
            carrier = sum_value // 10
            l1_reverse, l2_reverse = l1_reverse.next, l2_reverse.next

        while l1_reverse:
            sum_value = carrier + l1_reverse.val
            new_node = ListNode(sum_value % 10)
            node.next = new_node
            node = node.next
            carrier = sum_value // 10
            l1_reverse = l1_reverse.next

        while l2_reverse:
            sum_value = carrier + l2_reverse.val
            new_node = ListNode(sum_value % 10)
            node.next = new_node
            node = node.next
            carrier = sum_value // 10
            l2_reverse = l2_reverse.next

        if carrier:
            new_node = ListNode(carrier)
            node.next = new_node
            node = node.next
        node.next = None

        return prev.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        carrier = 0
        while l1 or l2 or carrier:
            val = carrier
            if l1:
                val += l1.val
                l1 = l1.next
            if l2:
                val += l2.val
                l2 = l2.next
            cur.next = ListNode(val % 10)
            cur = cur.next
            carrier = val // 10
        return dummy.next