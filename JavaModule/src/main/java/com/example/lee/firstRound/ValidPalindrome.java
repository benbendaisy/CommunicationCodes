package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 12/28/14.
 * Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
 * For example,
 * "A man, a plan, a canal: Panama" is a palindrome.
 * "race a car" is not a palindrome.
 * Note:
 * Have you consider that the string might be empty? This is a good question to ask during an interview.
 * For the purpose of this problem, we define empty string as valid palindrome.
 */
public class ValidPalindrome {
    public boolean isPalindrome(String s) {
        if(s == null || s.length() == 0 || s.length() == 1){
            return true;
        }

        String validStr = getValidateString(s);
        int left = 0, right = validStr.length() - 1;
        while(left < right){
            if(validStr.charAt(left) != validStr.charAt(right)){
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    private String getValidateString(String str){
        str = str.trim().toLowerCase();
        StringBuilder sb = new StringBuilder();
        int len = str.length();
        for(int i = 0; i < len; i++){
            char ch = str.charAt(i);
            if((ch >= 'a' && ch <= 'z') || (ch >= '0' && ch <= '9')){
                sb.append(ch);
            }
        }
        return sb.toString();
    }
}
