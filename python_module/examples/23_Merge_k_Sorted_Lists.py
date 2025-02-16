# Definition for singly-linked list.
from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
        You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

        Merge all the linked-lists into one sorted linked-list and return it.

        Example 1:

        Input: lists = [[1,4,5],[1,3,4],[2,6]]
        Output: [1,1,2,3,4,4,5,6]
        Explanation: The linked-lists are:
        [
          1->4->5,
          1->3->4,
          2->6
        ]
        merging them into one sorted list:
        1->1->2->3->4->4->5->6
        Example 2:

        Input: lists = []
        Output: []
        Example 3:

        Input: lists = [[]]
        Output: []
    """
    def mergeKLists1(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        v = []
        for i in lists:
            x = i
            while x:
                v += [x.val]
                x = x.next
        v = sorted(v, reverse=True)
        ans = None
        for i in v:
            ans = ListNode(i, ans)
        return ans

    def mergeKLists2(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge(l1, l2):
            dummy = ListNode(0)
            cur = dummy
            while l1 and l2:
                if l1.val < l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            cur.next = l1 or l2
            return dummy.next
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]

        mid = len(lists) // 2
        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        return merge(left, right)
    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_sort(left: int, right: int):
            if left == right:
                return lists[left]
            mid = left + (right - left) // 2
            left_list = merge_sort(left, mid)
            right_list = merge_sort(mid + 1, right)
            return merge(left_list, right_list)
        def merge(left_list: ListNode, right_list: ListNode):
            prev = head = ListNode()
            while left_list and right_list:
                if left_list.val < right_list.val:
                    head.next = left_list
                    left_list = left_list.next
                else:
                    head.next = right_list
                    right_list = right_list.next
                head = head.next
            if left_list:
                head.next = left_list
            if right_list:
                head.next = right_list
            return prev.next
        
        if not lists:
            return None
        return merge_sort(0, len(lists) - 1)