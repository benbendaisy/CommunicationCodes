# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    """
        Given a non-negative integer represented as a linked list of digits, plus one to the integer.

        The digits are stored such that the most significant digit is at the head of the list.

        Example 1:

        Input: head = [1,2,3]
        Output: [1,2,4]
        Example 2:

        Input: head = [0]
        Output: [1]

        Constraints:

        The number of nodes in the linked list is in the range [1, 100].
        0 <= Node.val <= 9
        The number represented by the linked list does not contain leading zeros except for the zero itself.
    """
    def plusOne1(self, head: ListNode) -> ListNode:
        parentDict = {head: None}
        node = head
        prev = node
        while node:
            prev = node
            node = node.next
            parentDict[node] = prev

        prev.val += 1
        hasPlus = False
        if prev.val > 9:
            prev.val -= 10
            cur = parentDict[prev]
            if not cur:
                return ListNode(1, head)
            while cur:
                if cur.val + 1 > 9:
                    cur.val -= 9
                    cur = parentDict[cur]
                    hasPlus = True
                else:
                    cur.val += 1
                    hasPlus = False
                    break

        return ListNode(1, head) if hasPlus else head

    def plusOne(self, head: ListNode) -> ListNode:
        if not head:
            return head

        sentinel = ListNode(0, head)
        notNine = sentinel
        node = head
        while node:
            if node.val != 9:
                notNine = node
            node = node.next

        notNine.val += 1
        notNine = notNine.next
        while notNine:
            notNine.val = 0
            notNine = notNine.next

        return sentinel if sentinel.val > 0 else sentinel.next

if __name__ == "__main__":
    head = ListNode(9)
    solution = Solution()
    ret = solution.plusOne(head)
    print(ret)




