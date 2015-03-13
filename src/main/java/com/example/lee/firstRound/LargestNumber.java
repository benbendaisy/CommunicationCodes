package com.example.lee.firstRound;

import java.util.Arrays;
import java.util.Comparator;

/**
 * Created by benbendaisy on 1/12/15.
 *
 * Given a list of non negative integers, arrange them such that they form the largest number.
 *
 * For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
 *
 * Note: The result may be very large, so you need to return a string instead of an integer.
 *
 * Credits:
 * Special thanks to @ts for adding this problem and creating all test cases.
 */
public class LargestNumber {
    public String largestNumber(int[] num) {
        if(num == null || num.length == 0){
            return "";
        } else if(num.length <= 1){
            return "" + num[0];
        }
        String[] newArray = new String[num.length];
        int i = 0;
        for (int value : num) {
            newArray[i++] = "" + value;
        }
        Arrays.sort(newArray, new StringComparator());
        StringBuilder sb = new StringBuilder();
        for(String n : newArray){
            sb.append(n);
        }
        String result = sb.toString();
        if(result.startsWith("00")){
            return "0";
        }
        return result;
    }


    private class StringComparator implements Comparator<String> {
        @Override
        public int compare(String str1, String str2) {
            if(str1.equals(str2)){
                return 0;
            }
            int left = 0, right = 0;
            while(left < str1.length() && right < str2.length() && str1.charAt(left) == str2.charAt(right)){
                left++;
                right++;
            }
            if(left < str1.length() && right < str2.length()){
                return str1.charAt(left) < str2.charAt(right) ? 1 : -1;
            } else if(left == str1.length() && right == str2.length()) {
                return 0;
            } else {
                if(left == str1.length()){
                    return compare(str1, str2.substring(right));
                } else {
                    return compare(str1.substring(left), str2);
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] num = {2060, 2};
        LargestNumber largestNumber = new LargestNumber();
        System.out.println(largestNumber.largestNumber(num));
    }
}
