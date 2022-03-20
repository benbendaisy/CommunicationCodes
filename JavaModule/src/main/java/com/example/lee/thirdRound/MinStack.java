package com.example.lee.thirdRound;

public class MinStack {
    private static class StackNode {
        int val;
        int min;
        StackNode prev;
    }

    StackNode head;
    /** initialize your data structure here. */
    public MinStack() {

    }

    public void push(int x) {
        if (head == null) {
            head = new StackNode();
            head.val = x;
            head.min = x;
        } else {
            StackNode node = new StackNode();
            node.val = x;
            node.min = Math.min(getMin(), x);
            node.prev = head;
            head = node;
        }
    }

    public void pop() {
        if (head == null) {
            return;
        }
        head = head.prev;
    }

    public int top() {
        if (head == null) {
            return -1;
        }
        return head.val;
    }

    public int getMin() {
        if (head == null) {
            return -1;
        }
        return head.min;
    }
}
