package com.example.lee.secondRound;

import java.util.Stack;

/**
 * Created by benbendaisy on 3/23/15.
 */
public class EvaluateReversePolishNotation {
    public int evalRPN(String[] tokens) {
        if (null == tokens || tokens.length < 1) {
            return 0;
        }

        Stack<Integer> stack = new Stack<Integer>();
        int idx = 0;
        while (idx < tokens.length) {
            String str = tokens[idx];
            if (isNumber(str)) {
                int num = Integer.parseInt(str);
                stack.push(num);
            } else {
                int b = stack.pop();
                int a = stack.pop();
                stack.push(calEquation(str, a, b));
            }
            idx++;
        }
        return stack.pop();
    }

    private boolean isNumber(String str) {
        if (null == str || "".equals(str)) {
            return false;
        }
        if (str.startsWith("-") || str.startsWith("+")) {
            str = str.substring(1);
        }
        if ("".equals(str)) return false;
        for (char ch : str.toCharArray()) {
            if (!Character.isDigit(ch)) {
                return false;
            }
        }
        return true;
    }

    private int calEquation(String op, int a, int b) {
        switch(op) {
            case "+": return a + b;
            case "-": return a - b;
            case "*": return a * b;
            case "/": return a / b;
        }
        return 0;
    }
}