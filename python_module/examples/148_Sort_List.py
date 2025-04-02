# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Given the head of a linked list, return the list after sorting it in ascending order.

    Example 1:

    Input: head = [4,2,1,3]
    Output: [1,2,3,4]
    Example 2:

    Input: head = [-1,5,3,4,0]
    Output: [-1,0,3,4,5]
    Example 3:

    Input: head = []
    Output: []
    """
    def sortList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time Limit Exceeded
        """
        if not head or not head.next:
            return head  # Edge case: empty list or single node
        
        dummy = ListNode(0)  # New dummy node for sorted list
        current = head  # Pointer to traverse the original list
        
        while current:
            prev, cur = dummy, dummy.next  # Start from the dummy node each time
            next_node = current.next  # Store next node
            
            # Find insertion point
            while cur and cur.val < current.val:
                prev = cur
                cur = cur.next
            
            # Insert current node into sorted position
            prev.next = current
            current.next = cur
            
            # Move to next node
            current = next_node
        
        return dummy.next
    
    def sortList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # Edge case: empty list or single node
        
        nums = []
        cur = head
        while cur:
            nums.append((cur.val, cur))
            cur = cur.next
        nums.sort(key=lambda x: x[0])
        for i in range(len(nums) - 1):
            nums[i][1].next = nums[i + 1][1]
        nums[-1][1].next = None
        return nums[0][1]
    
    def sortList3(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l1: ListNode, l2: ListNode) -> ListNode:
            dummy = ListNode()
            tail = dummy
            
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next, l1 = l1, l1.next
                else:
                    tail.next, l2 = l2, l2.next
                tail = tail.next
            
            tail.next = l1 if l1 else l2  # Append remaining elements
            return dummy.next
        
        if not head or not head.next:
            return head
        
        # Step 1: Find the middle of the list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None  # Split the list into two halves
        
        # Step 2: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)
        
        # Step 3: Merge the two sorted halves
        return merge(left, right)
    
    def sortList4(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l1: ListNode, l2: ListNode):
            dummy = ListNode()
            tail = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    tail.next = l1
                    l1 = l1.next
                    tail = tail.next
                else:
                    tail.next = l2
                    l2 = l2.next
                    tail = tail.next
            tail.next = l1 if l1 else l2
            return dummy.next
        
        if not head or not head.next:
            return head
        
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None

        left = self.sortList(head)
        right = self.sortList(mid)
        return merge(left, right)