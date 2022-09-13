# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
        Given the head of a singly linked list, return true if it is a palindrome.

        Example 1:

        Input: head = [1,2,2,1]
        Output: true
        Example 2:

        Input: head = [1,2]
        Output: false

        Constraints:

        The number of nodes in the list is in the range [1, 105].
        0 <= Node.val <= 9
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        return arr == arr[::-1]