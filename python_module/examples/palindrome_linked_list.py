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
        while head:
            arr.append(head.val)
            head = head.next
        l, r = 0, 0
        length = len(arr)
        if length % 2 == 0:
            l, r = length // 2 - 1, length // 2
        else:
            l = r = length // 2
        while l >= 0 and r < length:
            if arr[l] != arr[r]:
                return False
            l -= 1
            r += 1
        return True

    def reverse_link(self, head):
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    def isPalindrome1(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        cur = nxt = head
        while nxt and nxt.next:
            cur = cur.next
            nxt = nxt.next.next
        nxt = self.reverse_link(cur)
        cur = head
        while cur and nxt:
            if cur.val != nxt.val:
                return False
            cur = cur.next
            nxt = nxt.next
        return True


if __name__ == "__main__":
    four = ListNode(1)
    three = ListNode(2)
    two = ListNode(2)
    one = ListNode(1)
    one.next = two
    two.next = three
    three.next = four
    solution = Solution()
    ret = solution.isPalindrome1(one)
    print(ret)