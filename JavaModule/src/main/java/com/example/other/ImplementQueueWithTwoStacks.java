package com.example.other;

import java.util.Stack;

/**
 * Created by pzhong1 on 6/11/15.
 */
public class ImplementQueueWithTwoStacks {
    Stack<Integer> stack1 = new Stack<>();
    Stack<Integer> stack2 = new Stack<>();
    public void add(int x) {
        stack2.push(x);
    }

    public boolean isEmpty() {
        return stack1.isEmpty() && stack2.isEmpty();
    }

    public int poll() {
        if (stack1.isEmpty()) {
            while (!stack2.isEmpty()) {
                stack1.push(stack2.pop());
            }
        }
        if (!stack1.isEmpty()) return stack1.pop();
        return -1;
    }

    public int peek() {
        if (stack1.isEmpty()) {
            while (!stack2.isEmpty()) {
                stack1.push(stack2.pop());
            }
        }
        if (!stack1.isEmpty()) return stack1.peek();
        return -1;
    }

}
