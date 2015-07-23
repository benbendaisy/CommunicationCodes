package com.example.lee.secondRound;

import java.util.Stack;

/**
 * Created by benbendaisy on 6/22/15.
 */
public class BasicCalculatorII {
    public int calculate(String s) {
        if (null == s || s.length() < 1) return 0;
        String str = getPostPolish(s);
        return calculate(str.split(" "));
    }

    private String getPostPolish(String str) {
        StringBuilder sb = new StringBuilder();
        boolean isNumber = false;
        Stack<Character> stack = new Stack<Character>();
        for (char ch : str.toCharArray()) {
            if (isNumber(ch)) {
                if (isNumber) {
                    sb.append(ch);
                } else {
                    sb.append(' ');
                    sb.append(ch);
                    isNumber = true;
                }
            } else if (isOp(ch)) {
                while (!stack.isEmpty() && getLevel(stack.peek()) >= getLevel(ch)) {
                    sb.append(' ');
                    sb.append(stack.pop());
                }
                stack.push(ch);
                isNumber = false;
            }
        }
        while (!stack.isEmpty()) {
            sb.append(' ');
            sb.append(stack.pop());
        }
        return sb.toString().trim();
    }

    private boolean isNumber(char ch) {
        return ch >= '0' && ch <= '9';
    }

    private boolean isOp(char ch) {
        return ch == '-' || ch == '+' || ch == '*' || ch == '/';
    }

    private boolean isOp(String str) {
        return str.equals("-") || str.equals("+") || str.equals("*") || str.equals("/");
    }

    private int getLevel(char ch) {
        switch(ch) {
            case '-':
            case '+': return 0;
            case '*':
            case '/': return 1;
        }
        return 0;
    }

    private int calculate(String[] strs) {
        Stack<Long> stack = new Stack<Long>();
        for (String str : strs) {
            if (!isOp(str)) {
                stack.push(Long.parseLong(str));
            } else {
                long b = stack.pop();
                long a = stack.pop();
                stack.push(eval(a, b, str));
            }
        }
        return stack.pop().intValue();
    }

    private long eval(long a, long b, String str) {
        switch(str) {
            case "+": return a + b;
            case "-": return a - b;
            case "*": return a * b;
            case "/": return a / b;
        }
        return 0;
    }

    public static void main(String[] args) {
        BasicCalculatorII basicCalculatorII = new BasicCalculatorII();
        System.out.println(basicCalculatorII.calculate("3+2*2"));
    }
}
