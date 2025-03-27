# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

    Example 1:

    Input: head = [1,2,3,3,4,4,5]
    Output: [1,2,5]
    Example 2:

    Input: head = [1,1,1,2,3]
    Output: [2,3]
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        freq = defaultdict(int)
        cur = head
        while cur:
            freq[cur.val] += 1
            cur = cur.next
        dup_set = {key for key in freq if freq[key] > 1}

        dummy = ListNode()
        dummy.next = head
        prev, cur = dummy, head
        while cur:
            if cur.val in dup_set:
                prev.next = cur.next # delete the dup num
            else:
                prev = cur
            cur = cur.next
        return dummy.next