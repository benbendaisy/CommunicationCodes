# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

    Return the decimal value of the number in the linked list.

    The most significant bit is at the head of the linked list.

    Example 1:

    Input: head = [1,0,1]
    Output: 5
    Explanation: (101) in base 2 = (5) in base 10
    Example 2:

    Input: head = [0]
    Output: 0
    """
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        if not head:
            return 0
        
        cnt = 0
        while head:
            cnt = cnt * 2 + head.val
            head = head.next
        return cnt