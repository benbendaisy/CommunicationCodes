package com.example.lee.secondRound;

import java.util.LinkedList;
import java.util.Queue;

/**
 * Created by benbendaisy on 6/11/15.
 *
 * Implement the following operations of a stack using queues.
 *
 * push(x) -- Push element x onto stack.
 * pop() -- Removes the element on top of the stack.
 * top() -- Get the top element.
 * empty() -- Return whether the stack is empty.
 * Notes:
 * You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
 * Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
 * You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
 *
 */
public class ImplementStackusingQueues {
    Queue<Integer> queue1 = new LinkedList<Integer>();
    Queue<Integer> queue2 = new LinkedList<Integer>();
    // Push element x onto stack.
    public void push(int x) {
        if (!queue1.isEmpty()) {
            queue1.add(x);
        } else {
            queue2.add(x);
        }
    }

    // Removes the element on top of the stack.
    public void pop() {
        if (queue1.isEmpty()) {
            while (queue2.size() > 1) {
                queue1.add(queue2.poll());
            }
            if (!queue2.isEmpty()) queue2.poll();
        } else {
            while (queue1.size() > 1) {
                queue2.add(queue1.poll());
            }
            if (!queue1.isEmpty()) queue1.poll();
        }
    }

    // Get the top element.
    public int top() {
        int res = -1;
        if (queue1.isEmpty()) {
            while (queue2.size() > 1) {
                queue1.add(queue2.poll());
            }
            if (queue2.size() == 1) {
                res = queue2.poll();
                queue1.add(res);
            }
        } else {
            while (queue1.size() > 1) {
                queue2.add(queue1.poll());
            }
            if (queue1.size() == 1) {
                res = queue1.poll();
                queue2.add(res);
            }
        }
        return res;
    }


    public void pushI(int x) {
        queue2.add(x);
        while (!queue1.isEmpty()) {
            queue2.add(queue1.poll());
        }
        Queue<Integer> t = queue1;
        queue1 = queue2;
        queue2 = t;
    }

    public void popI() {
        if (!queue1.isEmpty()) queue1.poll();
    }

    // Return whether the stack is empty.
    public boolean empty() {
        return queue1.isEmpty() && queue2.isEmpty();
    }

    public int topI() {
        if (!queue1.isEmpty()) return queue1.peek();
        return -1;
    }

    public void pushII(int x) {
        queue1.add(x);
    }

    public void popII() {
        if (!queue1.isEmpty()) {
            while (queue1.size() > 1) {
                queue2.add(queue1.poll());
            }
            Queue<Integer> t = queue1;
            queue1 = queue2;
            queue2 = t;
        }
    }

    // Return whether the stack is empty.
    public boolean emptyII() {
        return queue1.isEmpty() && queue2.isEmpty();
    }

    public int topII() {
        int res = -1;
        if (!queue1.isEmpty()) {
            while (queue1.size() > 1) {
                queue2.add(queue1.poll());
            }
            res = queue1.poll();
            queue2.add(res);
            Queue<Integer> t = queue1;
            queue1 = queue2;
            queue2 = t;
        }
        return res;
    }
}
