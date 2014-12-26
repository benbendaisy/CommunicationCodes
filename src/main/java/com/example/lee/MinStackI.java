package com.example.lee;

import java.util.LinkedList;
import java.util.List;

/**
 * Created by pzhong1 on 12/26/14.
 */
public class MinStackI {
    private List<Integer> stack = new LinkedList<Integer>();
    private List<Integer> minStack = new LinkedList<Integer>();
    public void push(int x) {
        stack.add(0,x);
        if((!minStack.isEmpty() && minStack.get(0) >= x) || minStack.isEmpty()){
            minStack.add(0, x);
        }
    }

    public void pop() {
        if(!stack.isEmpty()){
            int x = stack.get(0);
            int min = minStack.get(0);
            if(x == min){
                minStack.remove(0);
            }
            stack.remove(0);
        }
    }

    public int top() {
        if(!stack.isEmpty()){
            return stack.get(0);
        } else {
            return -1;
        }
    }

    public int getMin() {
        if(!minStack.isEmpty()){
            return minStack.get(0);
        } else {
            return -1;
        }
    }
}
