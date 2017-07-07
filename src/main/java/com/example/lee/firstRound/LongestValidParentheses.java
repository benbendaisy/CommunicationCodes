package com.example.lee.firstRound;

import java.util.Stack;

/**
 * Created by benbendaisy on 2/26/15.
 *
 * Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
 *
 * For "(()", the longest valid parentheses substring is "()", which has length = 2.
 *
 * Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.
 */
public class LongestValidParentheses {

    /*
    * use a stack to record the position of each '(' and use last to save the position
    * that valid substring starts
    */
    public int longestValidParentheses(String s) {
        if (null == s || s.length() == 0) {
            return 0;
        }

        Stack<Integer> stack = new Stack<>();
        int last = -1, max = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                stack.push(i);
            } else {
                if (stack.isEmpty()) {
                    //recoard the position before first valid '('
                    last = i;
                } else {
                    //pop up a '(' to match current ')'
                    stack.pop();
                    //if stack is empty, the substring after the postion last is valid
                    if (stack.isEmpty()) {
                        max = Math.max(i - last, max);
                    } else {
                        //if stack is not empty, the substring after previous '(' is valid
                        max = Math.max(i - stack.peek(), max);
                    }
                }
            }
        }
        return max;
    }

    public static void main(String[] args) {
        LongestValidParentheses longestValidParentheses = new LongestValidParentheses();
        System.out.println(longestValidParentheses.longestValidParentheses("()(()"));
    }
}
