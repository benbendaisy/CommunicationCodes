package com.example.lee.thirdRound;

import java.util.Stack;

public class EvaluateReversePolishNotation {
    public int evalRPN(String[] tokens) {
        if (tokens == null || tokens.length == 0) {
            return -1;
        }
        Stack<Integer> numberStack = new Stack<>();
        int idx = 0;
        while (idx < tokens.length) {
            if (!isOperator(tokens[idx])) {
                numberStack.push(Integer.parseInt(tokens[idx]));
            } else {
                int b = numberStack.pop();
                int a = numberStack.pop();
                numberStack.push(calculateExpression(a, b, tokens[idx]));
            }
            idx++;
        }
        return numberStack.pop();
    }

    private int getOperatorPriority(String opr) {
        switch (opr) {
            case "+":
            case "-": return 1;
            case "*":
            case "/": return 2;
        }
        return -1;
    }

    private boolean isOperator(String str) {
        return "+".equals(str) || "-".equals(str) || "*".equals(str) || "/".equals(str);
    }

    private int calculateExpression(int a, int b, String str) {
        switch (str) {
            case "+": return a + b;
            case "-": return a - b;
            case "*": return a * b;
            case "/": return a / b;
        }
        return -1;
    }

    public static void main(String[] args) {
        EvaluateReversePolishNotation evaluateReversePolishNotation = new EvaluateReversePolishNotation();
        String[] tokens = {"2","1","+","3","*"};
        System.out.println(evaluateReversePolishNotation.evalRPN(tokens));
    }
}
