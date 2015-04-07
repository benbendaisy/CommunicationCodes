package com.example.lee.firstRound;

import java.util.Stack;

/**
 * Created by benbendaisy on 12/19/14.
 * Evaluate the value of an arithmetic expression in Reverse Polish Notation.
 * Valid operators are +, -, *, /. Each operand may be an integer or another expression.
 * Some examples:
 * ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
 * ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
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
            if (isInteger(str)) {
                stack.push(Integer.parseInt(str));
            } else if (isOperator(str)) {
                int b = stack.pop();
                int a = stack.pop();
                int res = execEquation(str, a, b);
                stack.push(res);
            }
            idx++;
        }
        return stack.pop();
    }

    private boolean isOperator(String str) {
        switch (str) {
            case "+":
            case "-":
            case "*":
            case "/": return true;
        }
        return false;
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

    private boolean isInteger(String str) {
        try {
            int it = Integer.parseInt(str);
        } catch (NumberFormatException e) {
            return false;
        }
        return true;
    }

    private int execEquation(String str, int a, int b) {
        switch (str) {
            case "+": return a + b;
            case "-": return a - b;
            case "*": return a * b;
            case "/": return a / b;
        }
        return 0;
    }

    public static void main(String[] args) {
        EvaluateReversePolishNotation evaluateReversePolishNotation = new EvaluateReversePolishNotation();
        String[] tokens = {"3", "-4", "+"};
        System.out.println(evaluateReversePolishNotation.evalRPN(tokens));
    }
}
