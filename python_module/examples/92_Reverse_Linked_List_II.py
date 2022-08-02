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
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
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
