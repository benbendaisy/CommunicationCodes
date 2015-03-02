package com.example.lee;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by benbendaisy on 2/8/15.
 *
 * The count-and-say sequence is the sequence of integers beginning as follows:
 * 1, 11, 21, 1211, 111221, ...
 *
 * 1 is read off as "one 1" or 11.
 * 11 is read off as "two 1s" or 21.
 * 21 is read off as "one 2, then one 1" or 1211.
 * Given an integer n, generate the nth sequence.
 *
 * Note: The sequence of integers will be represented as a string.
 */
public class CountandSay {
    public String countAndSay(int n) {
        if(n < 1){
            return "";
        } else if(n == 1){
            return "1";
        }

        String str = "1";
        n--;
        char ch = str.charAt(0);
        while(n > 0){
            String newStr = "";
            ch = str.charAt(0);
            int count = 1;
            for(int i = 1; i < str.length(); i++){
                if(str.charAt(i) != ch){
                    newStr += count + "" + ch;
                    count = 0;
                }
                count++;
                ch = str.charAt(i);
            }
            str = newStr + count + "" + ch;
            n--;
        }
        return str;
    }

    public static void main(String[] args) {
        CountandSay countandSay = new CountandSay();
        System.out.println(countandSay.countAndSay(4));
        Set<Integer> set = new HashSet<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9));

    }
}
