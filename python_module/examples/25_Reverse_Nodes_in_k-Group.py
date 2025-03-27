# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

    k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

    You may not alter the values in the list's nodes, only nodes themselves may be changed.

    Example 1:

    Input: head = [1,2,3,4,5], k = 2
    Output: [2,1,4,3,5]
    Example 2:

    Input: head = [1,2,3,4,5], k = 3
    Output: [3,2,1,4,5]
    """
    def reverseKGroup1(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        def reverse(start: ListNode, k: int):
            prev, cur = None, start
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev, start  # prev is new head, start is new tail
        
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        cur = head
        
        while True:
            # Check if there are at least k nodes left
            count = 0
            temp = cur
            while temp and count < k:
                temp = temp.next
                count += 1
            if count < k:
                break  # Not enough nodes to reverse
            
            # Reverse k nodes
            new_head, new_tail = reverse(cur, k)
            prev_group.next = new_head
            new_tail.next = temp
            
            # Move prev_group and cur forward
            prev_group = new_tail
            cur = temp

        return dummy.next

    def reverseKGroup2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(start):
            key = k
            prev, curr = None, start
            while key > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                key -= 1
            return prev
        
        count = 0
        ptr = head
        while ptr and count < k:
            ptr = ptr.next
            count += 1
        
        if count == k:
            new_head = reverseLinkedList(head)
            head.next = self.reverseKGroup(ptr, k)
            return new_head
        
        return head
    
    def reverseKGroup3(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        
        def reverse(start: ListNode):
            prev, cur = None, start
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev, start  # prev is new head, start is new tail
        dummy = ListNode(0)
        dummy.next = head
        prev_group = dummy
        cur = head

        while True:
            cnt = 0
            temp = cur
            while temp and cnt < k:
                temp = temp.next
                cnt += 1
            if cnt < k:
                break
            new_head, new_tail = reverse(cur)
            prev_group.next = new_head
            new_tail.next = temp
            prev_group = new_tail
            cur = temp
        return dummy.next

    def reverseKGroup4(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head
        
        def reverse(start: ListNode):
            prev, cur = None, start
            for _ in range(k):
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev, start # prev is the new start and start is the new end
        
        dummy = ListNode()
        dummy.next = head
        prev_group = dummy
        cur = head
        while True:
            temp = cur
            cnt = 0
            while temp and cnt < k:
                temp = temp.next
                cnt += 1
            
            if cnt < k:
                break
            
            new_head, new_tail = reverse(cur)
            prev_group.next = new_head
            prev_group = new_tail
            new_tail.next = temp
            cur = temp
        return dummy.next