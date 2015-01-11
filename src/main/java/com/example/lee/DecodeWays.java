package com.example.lee;

/**
 * Created by benbendaisy on 1/10/15.
 *
 * A message containing letters from A-Z is being encoded to numbers using the following mapping:
 *
 * 'A' -> 1
 * 'B' -> 2
 * ...
 * 'Z' -> 26
 * Given an encoded message containing digits, determine the total number of ways to decode it.
 *
 * For example,
 * Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
 *
 * The number of ways decoding "12" is 2.
 */
public class DecodeWays {
    //dp is used to save the number of decoding ways starting from beginning
    public int numDecodings(String s) {
        if(s == null || s.isEmpty() || (s.length() == 1 && "0".equals(s))){
            return 0;
        } else if(s.length() == 1 && !"0".equals(s)){
            return 1;
        } else if(s.indexOf("00") != -1 || s.startsWith("0")){
            return 0;
        }
        int len = s.length();
        int[] dp = new int[len + 1];
        dp[0] = 1;
        for(int i = 1; i <= len; i++){
            if(i - 2 >= 0 && s.charAt(i - 1) == '0' && s.charAt(i - 2) >= '3'){
                return 0;
            }else if(s.charAt(i - 1) == '0'){
                if(i - 2 >= 0){
                    dp[i - 1] = dp[i - 2];
                } else {
                    dp[i - 1] = dp[i - 1] - 1;
                }
                dp[i] = dp[i - 1];
                continue;
            }
            if(i - 2 >= 0){
                if((s.charAt(i - 2) == '2' && s.charAt(i - 1) <= '6') || (s.charAt(i - 2) == '1' && s.charAt(i - 1) != '0')){
                    dp[i] = dp[i-1] + dp[i-2];
                } else {
                    dp[i] = dp[i-1];
                }
            } else {
                dp[i] = dp[i-1];
            }
        }

        return dp[len];
    }

    public int numDecodingsI(String s) {
        if(s == null || s.isEmpty() || (s.length() == 1 && "0".equals(s))){
            return 0;
        } else if(s.length() == 1 && !"0".equals(s)){
            return 1;
        } else if(s.indexOf("00") != -1 || s.startsWith("0")){
            return 0;
        }
        return numDecodingsHelper(s, s.length() - 1);
    }

    private int numDecodingsHelper(String str, int current){
        int len = str.length();
        if(current == 0){
            return 1;
        } else if(current < 0){
            return 0;
        } else if(str.charAt(current) == '0'){
            if(current >= 1 && str.charAt(current - 1) >= '3'){
                return 0;
            } else {
                return numDecodingsHelper(str, current - 1);
            }
        } else if(current >= 1) {
            if(str.charAt(current) >= '1' && (str.charAt(current - 1) == '2' && str.charAt(current) <= '6') || (str.charAt(current - 1) == '1' && str.charAt(current) != '0')){
                return numDecodingsHelper(str, current - 1) + numDecodingsHelper(str, current - 2);
            }
        }

        return numDecodingsHelper(str, current - 1);
    }

    public static void main(String[] args) {
        DecodeWays decodeWays = new DecodeWays();
        System.out.println(decodeWays.numDecodingsI("101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010"));
    }
}
