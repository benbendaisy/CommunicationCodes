package com.example.lee.thirdRound;

import com.example.lee.model.ListNode;

import java.util.HashSet;
import java.util.Set;

public class IntersectionOfTwoLinkedLists {
    /**
     * O(m + n) with O(m) or O(n) space complexity solution
     * @param headA
     * @param headB
     * @return
     */
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }
        Set<ListNode> nodeSet = new HashSet<>();
        while (headA != null) {
            nodeSet.add(headA);
            headA = headA.next;
        }

        while (headB != null) {
            if (!nodeSet.add(headB)) {
                return headB;
            }
            headB = headB.next;
        }
        return null;
    }

    public ListNode getIntersectionNodeI(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }
        ListNode pa = headA;
        ListNode pb = headB;
        while (pa != null && pb != null) {
            if (pa == pb) {
                return pa;
            }
            pa = pa.next;
            pb = pb.next;
            if (pa == pb) {
                return pa;
            } else if (pa == null) {
                pa = headB;
            } else if (pb == null) {
                pb = headA;
            }
        }
        return null;
    }

    public ListNode getIntersectionNodeII(ListNode headA, ListNode headB) {
        if (headA == null || headB == null) {
            return null;
        }
        int lenA = 0;
        ListNode pa = headA;
        while (pa != null) {
            lenA++;
            pa = pa.next;
        }
        int lenB = 0;
        ListNode pb = headB;
        while (pb != null) {
            pb = pb.next;
            lenB++;
        }
        if (lenA > lenB) {
            int diff = lenA - lenB;
            while (diff > 0) {
                headA = headA.next;
                diff--;
            }
        } else if (lenB > lenA) {
            int diff = lenB - lenA;
            while (diff > 0) {
                headB = headB.next;
                diff--;
            }
        }
        while (headA != null && headB != null) {
            if (headA == headB) {
                return headA;
            }
            headA = headA.next;
            headB = headB.next;
        }
        return null;
    }
}
