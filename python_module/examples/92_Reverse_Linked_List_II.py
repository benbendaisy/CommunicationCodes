# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    """
        Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

        Example 1:

        Input: head = [1,2,3,4,5], left = 2, right = 4
        Output: [1,4,3,2,5]
        Example 2:

        Input: head = [5], left = 1, right = 1
        Output: [5]

        Constraints:

        The number of nodes in the list is n.
        1 <= n <= 500
        -500 <= Node.val <= 500
        1 <= left <= right <= n
    """
    def reverseBetween1(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        cur, prev = head, None
        while left > 1:
            prev = cur
            cur = cur.next
            left -= 1
            right -= 1

        tail, con = cur, prev
        while right > 0:
            t = cur.next
            cur.next = prev
            prev = cur
            cur = t
            right -= 1
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = cur
        return head
    
    def reverseBetween2(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        idx = 1
        dummy = ListNode()
        dummy.next = head
        reverse_start = dummy
        while reverse_start.next and idx < left:
            reverse_start = reverse_start.next
            idx += 1
        prev = reverse_start
        cur = reverse_start.next
        while cur and idx <= right:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            idx += 1
        reverse_start.next.next = cur
        reverse_start.next = prev
        return dummy.next

    def reverseBetween3(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverse(n1: ListNode, n2: ListNode) -> ListNode:
            prev, cur = None, n1
            while cur and cur != n2:
                t = cur.next
                cur.next = prev
                prev = cur
                cur = t
            return prev
        
        dummy = ListNode()
        dummy.next = head
        cur = head if left != 1 else dummy
        idx = 1 if left != 1 else 0
        while cur:
            if cur.next and idx == left - 1:
                curr = cur.next
                idx += 1
                while curr and idx < right:
                    idx += 1
                    curr = curr.next
                l1, r1 = cur.next, curr.next
                cur.next = reverse(cur.next, r1)
                l1.next = r1
            cur = cur.next
            idx += 1
        return dummy.next
    
    def reverseBetween4(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        reverse_start = dummy
        idx = 1
        while reverse_start.next and idx < left:
            reverse_start = reverse_start.next
            idx += 1
        prev = reverse_start
        cur = reverse_start.next
        while cur and idx <= right:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            idx += 1
        reverse_start.next.next = cur
        reverse_start.next = prev
        return dummy.next
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        def reverse(start: ListNode):
            prev, cur = None, start
            for _ in range(left, right + 1):
                if cur:
                    nxt = cur.next
                    cur.next = prev
                    prev = cur
                    cur = nxt
            return prev, cur # new head and cur is the next head
        
        dummy = ListNode()
        dummy.next = head
        cur, prev = head, dummy
        idx = 1
        while idx < left and cur:
            cur = cur.next
            prev = prev.next
            idx += 1

        new_head, next_head = reverse(cur)
        prev.next = new_head
        cur.next = next_head
        return dummy.next

if __name__ == "__main__":
    # head = ListNode(1)
    # two = ListNode(2)
    three = ListNode(3)
    # four = ListNode(4)
    five = ListNode(5)
    # head.next = two
    # two.next = three
    # three.next = four
    # four.next = five

    three.next = five
    head = three
    solution = Solution()
    ret = solution.reverseBetween(head, 1, 2)
    print(ret)
