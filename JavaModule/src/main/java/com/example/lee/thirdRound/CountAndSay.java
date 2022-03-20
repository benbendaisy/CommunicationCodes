package com.example.lee.thirdRound;

import java.util.stream.IntStream;

/**
 * Created by benbendaisy on 7/6/17.
 */
public class CountAndSay {
    public String countAndSay(int n) {
        if (n < 1) {
            return "";
        }
        String res = "1";
        while (n > 1) {
            StringBuilder sb = new StringBuilder();
            int idx = 0;
            while (idx < res.length()) {
                int count = 1;
                char ch = res.charAt(idx);
                // increase the index to the last character that is same to previous character
                while (idx < res.length() - 1 && res.charAt(idx) == res.charAt(idx + 1)) {
                    count++;
                    idx++;
                }
                sb.append(count);
                sb.append(ch);
                idx++;
            }
            res = sb.toString();
            n--;
        }
        return res;
    }

    public static void main(String[] args) {
        CountAndSay countAndSay = new CountAndSay();
        IntStream.range(1, 6).forEach(i -> System.out.println(countAndSay.countAndSay(i)));
    }
}
