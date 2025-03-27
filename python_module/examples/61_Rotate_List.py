# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Given the head of a linked list, rotate the list to the right by k places.

    Example 1:

    Input: head = [1,2,3,4,5], k = 2
    Output: [4,5,1,2,3]
    Example 2:

    Input: head = [0,1,2], k = 4
    Output: [2,0,1]
    """
    def rotateRight1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        def rotate(cur: ListNode):
            dummy = ListNode()
            dummy.next = cur
            prev = dummy
            while cur.next:
                cur = cur.next
                prev = prev.next
            prev.next = None
            nxt = dummy.next
            dummy.next = cur
            cur.next = nxt
            return dummy.next
        
        dummy = ListNode()
        dummy.next = head
        while k > 0:
            dummy.next = rotate(dummy.next)
            k -= 1
        return dummy.next
    
    def rotateRight2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        # Step 1: Compute length of the list
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1

        # Step 2: Optimize k
        k = k % length
        if k == 0:
            return head  # No rotation needed

        # Step 3: Find the new head (at position length - k)
        prev = head
        for _ in range(length - k - 1):
            prev = prev.next

        # Step 4: Update pointers
        new_head = prev.next
        prev.next = None
        tail.next = head  # Connect original tail to original head

        return new_head
    
    def rotateRight3(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        
        length = 1
        tail = head
        while tail.next:
            tail = tail.next
            length += 1
        
        k = k % length
        if k == 0:
            return head
        prev = head
        for _ in range(length - k - 1):
            prev = prev.next
        new_head = prev.next
        prev.next = None
        tail.next = head
        return new_head