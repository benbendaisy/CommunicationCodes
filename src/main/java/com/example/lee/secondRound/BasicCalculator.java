package com.example.lee.secondRound;

import java.util.Stack;

/**
 * Created by benbendaisy on 6/10/15.
 */
public class BasicCalculator {
    public int calculate(String s) {
        if (null == s || s.length() < 1) return 0;
        StringBuilder sb = new StringBuilder();
        Stack<Character> stack = new Stack<Character>();
        boolean isChar = false;
        for (char ch : s.toCharArray()) {
            if (isChar(ch)) {
                if (isChar) {
                    sb.append(ch);
                } else {
                    sb.append(" ");
                    sb.append(ch);
                    isChar = true;
                }
            } else if (isOp(ch)) {
                isChar = false;
                while (!stack.isEmpty() && stack.peek() != '(') {
                    sb.append(" ");
                    sb.append(stack.pop());
                }
                stack.push(ch);
            } else if (ch == ')') {
                isChar = false;
                while (!stack.isEmpty() && stack.peek() != '(') {
                    sb.append(" ");
                    sb.append(stack.pop());
                }
                if (!stack.isEmpty()) stack.pop();
            } else if (ch == '(') {
                isChar = false;
                stack.push(ch);
            }
        }
        if (!stack.isEmpty()) {
            sb.append(" ");
            sb.append(stack.pop());
        }
        String postStr = sb.toString().trim();
        Stack<String> stk = new Stack<String>();
        String[] tokens = postStr.split(" ");
        for (String token : tokens) {
            if (isChar(token)) {
                stk.push(token);
            } else if (isOp(token)) {
                String b = stk.pop();
                String a = stk.pop();
                stk.push(exec(a, b, token));
            }
        }
        String res = "";
        while (!stk.isEmpty()) {
            res += stk.pop();
        }
        return Integer.parseInt(res);
    }

    private boolean isChar(char ch) {
        return ch >= '0' && ch <= '9';
    }

    private boolean isChar(String str) {
        try {
            Integer.parseInt(str);
        } catch (Exception e) {
            return false;
        }
        return true;
    }

    private boolean isOp(char ch) {
        return ch == '+' || ch == '-';
    }

    private boolean isOp(String str) {
        return "+".equals(str) || "-".equals(str);
    }

    private String exec(String a, String b, String op) {
        int x = Integer.parseInt(a);
        int y = Integer.parseInt(b);
        int z = 0;
        switch (op) {
            case "+" : z = x + y; break;
            case "-" : z = x - y; break;
        }
        return String.valueOf(z);
    }

    public static void main(String[] args) {
        BasicCalculator calculator = new BasicCalculator();
        System.out.println(calculator.calculate("2-4-(8+2-6+(8+4-(1)+8-10))"));
    }
}
