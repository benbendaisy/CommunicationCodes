package com.example.lee.firstRound;

import java.util.*;

/**
 * Created by benbendaisy on 2/26/15.
 *
 * Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
 *
 * For example, given n = 3, a solution set is:
 *
 * "((()))", "(()())", "(())()", "()(())", "()()()"
 */
public class GenerateParentheses {
    public List<String> generateParenthesis(int n) {
        List<String> list = new ArrayList<String>();
        if (n <= 0) {
            return list;
        }
        list.add("()");
        generateParenthesis(n, list);
        return list;
    }


    public void generateParenthesis(int n, List<String> list) {
        if (n <= 1) {
            return;
        }

        Set<String> set = new HashSet<String>();
        for (String str : list) {
            for (int i = 0; i < str.length(); i++) {
                set.add(str.substring(0, i) + "()" + str.substring(i));
            }
        }

        list.clear();
        list.addAll(set);

        generateParenthesis(n - 1, list);
    }

    public static void main(String[] args) {
        GenerateParentheses generateParentheses = new GenerateParentheses();
        System.out.println(generateParentheses.generateParenthesis(3));
    }

}
