package com.example.ip;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

/**
 * Created by benbendaisy on 5/27/15.
 */
public class PermutationsI {
    public void printPerm(String charset, int num_chars) {
        if (null == charset || charset.length() == 0 || charset.length() < num_chars || num_chars <= 0) return;
        Set<String> set = new HashSet<String>();
        Set<Integer> setI = new HashSet<Integer>();
        List<Character> list = new ArrayList<Character>();
        printPerm(charset, num_chars, set, list, setI);

        for (String string : set) {
            System.out.println(string);
        }
    }


    private void printPerm(String charSet, int num, Set<String> set, List<Character> list, Set<Integer> setI) {
        if (list.size() == num) {
            StringBuilder sb = new StringBuilder();
            for(char ch : list) sb.append(ch + ", ");
            sb.deleteCharAt(sb.length() - 1);
            set.add(sb.toString());
            return;
        }


        for (int i = 0; i < charSet.length(); i++) {
            Set<Integer> newSetI = new HashSet<Integer>(setI);
            List<Character> newList = new ArrayList<Character>(list);
            if (newSetI.add(i)) {
                newList.add(charSet.charAt(i));
                printPerm(charSet, num, set, newList, newSetI);
            }
        }
    }

    public static void main(String[] args) {
        PermutationsI solution = new PermutationsI();
        solution.printPerm("abc", 3);
    }
}
