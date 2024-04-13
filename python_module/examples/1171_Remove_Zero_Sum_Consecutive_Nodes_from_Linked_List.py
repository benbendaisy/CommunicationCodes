# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
    Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.

    After doing so, return the head of the final linked list.  You may return any such answer.

    (Note that in the examples below, all sequences are serializations of ListNode objects.)

    Example 1:

    Input: head = [1,2,-3,3,1]
    Output: [3,1]
    Note: The answer [1,2,1] would also be accepted.
    Example 2:

    Input: head = [1,2,3,-3,4]
    Output: [1,2,4]
    Example 3:

    Input: head = [1,2,3,-3,-2]
    Output: [1]
    """
    def removeZeroSumSublists1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        start = front
        while start:
            prefix_sum = 0
            end = start.next
            while end:
                prefix_sum += end.val
                if prefix_sum == 0:
                    start.next = end.next
                end = end.next
            start = start.next
        return front.next
    
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        front = ListNode(0, head)
        cur = front
        prefix_sum = 0
        pre_sum_to_node = {0: front}
        while cur:
            prefix_sum += cur.val
            pre_sum_to_node[prefix_sum] = cur
            cur = cur.next
        prefix_sum = 0
        cur = front

        while cur:
            prefix_sum += cur.val
            cur.next = pre_sum_to_node[prefix_sum].next
            cur = cur.next
        return front.next