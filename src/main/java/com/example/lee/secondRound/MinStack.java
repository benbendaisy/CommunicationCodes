package com.example.lee.secondRound;

import java.util.Stack;

/**
 * Created by benbendaisy on 3/18/15.
 */
public class MinStack {
    private Stack<Element> stack = new Stack<Element>();
    public void push(int x) {
        Element el = new Element();
        el.element = x;
        if (!stack.isEmpty()) {
            Element elt = stack.peek();
            if (elt.min > x) {
                el.min = x;
            } else {
                el.min = elt.min;
            }
        } else {
            el.min = x;
        }
        stack.push(el);
    }

    public void pop() {
        if (stack.isEmpty()) {
            return;
        }
        stack.pop();
    }

    public int top() {
        if (stack.isEmpty()) {
            return -1;
        }
        return stack.peek().element;
    }

    public int getMin() {
        if (stack.isEmpty()) {
            return -1;
        }
        return stack.peek().min;
    }

    private class Element {
        public int element;
        public int min;
    }
}
