# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
        Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

        The first node is considered odd, and the second node is even, and so on.

        Note that the relative order inside both the even and odd groups should remain as it was in the input.

        You must solve the problem in O(1) extra space complexity and O(n) time complexity.

        Example 1:

        Input: head = [1,2,3,4,5]
        Output: [1,3,5,2,4]
        Example 2:

        Input: head = [2,1,3,5,6,4,7]
        Output: [2,3,6,7,1,5,4]

        Constraints:

        The number of nodes in the linked list is in the range [0, 104].
        -106 <= Node.val <= 106
    """
    def oddEvenList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddHead = head
        if not head or not head.next:
            return head

        evenHead = head.next
        oddCur, evenCur = oddHead, evenHead
        cnt = 1
        cur = evenHead.next
        while cur:
            if cnt % 2 == 0:
                evenCur.next = cur
                evenCur = cur
            else:
                oddCur.next = cur
                oddCur = cur
            cur = cur.next
            cnt += 1

        oddCur.next = evenHead
        evenCur.next = None
        return head

    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev_odd = odd = ListNode(0)
        prev_even = even = ListNode(0)
        cur = head
        idx = 0
        while cur:
            if idx % 2 == 0:
                odd.next = cur
                odd = odd.next
            else:
                even.next = cur
                even = even.next
            cur = cur.next
            idx += 1
        odd.next = prev_even.next
        even.next = None
        return prev_odd.next
