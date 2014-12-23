package com.example.lee;

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
        if(tokens == null || tokens.length == 0){
            return 0;
        } else if(tokens.length == 1){
            return Integer.parseInt(tokens[0]);
        }
        Stack<String> st = new Stack<String>();
        for(int i = 0; i < tokens.length; i++){
            if(isValidNumber(tokens[i])){
                st.push(tokens[i]);
            } else {
                int result = 0;
                String second = st.pop();
                String first = st.pop();
                char type = tokens[i].charAt(0);
                switch(type){
                    case '+':
                        result = Integer.parseInt(first) + Integer.parseInt(second);
                        break;
                    case '-':
                        result = Integer.parseInt(first) - Integer.parseInt(second);
                        break;
                    case '*':
                        result = Integer.parseInt(first) * Integer.parseInt(second);
                        break;
                    case '/':
                        result = Integer.parseInt(first) / Integer.parseInt(second);
                        break;
                    default: break;
                }

                if(st.isEmpty()){
                    return result;
                } else {
                    st.push( String.valueOf(result));
                }
            }
        }
        return 0;
    }

    public boolean isValidNumber(String s) {
        return s.matches("[-+]?\\d*\\.?\\d+");
    }
}
