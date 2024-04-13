# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeInBetween1(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        merge_array = []
        idx = 0
        cur1 = list1
        while idx < a:
            merge_array.append(cur1.val)
            cur1 = cur1.next
            idx += 1
        
        cur2 = list2
        while cur2:
            merge_array.append(cur2.val)
            cur2 = cur2.next
        while idx < b + 1:
            cur1 = cur1.next
            idx += 1
        
        while cur1:
            merge_array.append(cur1.val)
            cur1 = cur1.next
        
        result_list = None
        for i in range(len(merge_array)):
            new_node = ListNode(merge_array.pop(), result_list)
            result_list = new_node
        return result_list
    
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        start = ListNode()
        end = list1

        for idx in range(b):
            if idx == a - 1:
                start = end
            end = end.next
        start.next = list2

        while list2.next:
            list2 = list2.next
        list2.next = end.next
        end.next = None
        return list1