package com.example.lee.firstRound;

import java.util.Stack;

/**
 * Created by benbendaisy on 3/2/15.
 *
 * Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
 *
 * The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
 */
public class ValidParentheses {
    public boolean isValid(String s) {
        if (null == s || s.length() < 2) {
            return false;
        }

        Stack<Character> stack = new Stack<Character>();
        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == '(' || ch == '[' || ch == '{' ) {
                stack.push(ch);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }
                switch (stack.pop()) {
                    case '(':
                        if (ch != ')') return false;
                        break;
                    case '[':
                        if (ch != ']') return false;
                        break;
                    case '{':
                        if (ch != '}') return false;
                        break;
                }
            }
        }
        return stack.isEmpty();
    }
}
