package com.example.lee.thirdRound;

import java.util.Stack;

/**
 * Created by benbendaisy on 6/30/17.
 */
public class ValidParentheses {
    public boolean isValid(String s) {
        if (s == null || s.length() < 2) {
            return false;
        }
        Stack<Character> stack = new Stack<>();
        stack.push(s.charAt(0));
        int idx = 1;
        while (idx < s.length()) {
            Character ch;
            switch (s.charAt(idx)) {
                case ')':
                    if (stack.isEmpty()) {
                        return false;
                    }
                     ch = stack.pop();
                     if (ch != '(') {
                         return false;
                     }
                     break;
                case ']':
                    if (stack.isEmpty()) {
                        return false;
                    }
                    ch = stack.pop();
                    if (ch != '[') {
                        return false;
                    }
                    break;
                case '}':
                    if (stack.isEmpty()) {
                        return false;
                    }
                    ch = stack.pop();
                    if (ch != '{') {
                        return false;
                    }
                    break;
                case '(':
                case '[':
                case '{':
                    stack.push(s.charAt(idx));
                    break;
                default:
                    return false;
            }
            idx++;
        }
        return stack.isEmpty() && idx == s.length();
    }
}
