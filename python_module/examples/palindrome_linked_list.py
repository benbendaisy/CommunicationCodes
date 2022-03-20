# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        arr = []
        length = len(arr)
        while not head:
            arr.append(head.val)
            head = head.next
        l, r = 0, 0
        if length % 2 == 0:
            l, r = length // 2 - 1, length // 2
        else:
            l, r = length // 2
        while l > 0 and r < length:
            if arr[l] != arr[r]:
                return False
            l -= 1
            r += 1

    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
            if not head or not head.next:
                return True
            cur = nxt = head
            while not nxt.next:
                cur = cur.next
                nxt = nxt.next.next
            nxt = cur.next
            left = head
            while left.next != cur:
                right = left.next
                temp = right.next
                right.next = left
                left = temp
            cur.next = left

            while not cur and not nxt:
                if cur.val != nxt.val:
                    return False
                cur = cur.next
                nxt = nxt.next