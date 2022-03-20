package com.example.lee.thirdRound;

import java.util.HashMap;
import java.util.Map;

/**
 * Created by benbendaisy on 6/21/17.
 */
public class LongestPalindrome {
    /**
     * O(n^2) solution accepted by leetcode
     * @param s
     * @return
     */
    public String longestPalindrome(String s) {
        if (s == null || s.length() == 0) {
            return s;
        }
        String longestString = "";
        for (int i = 0; i < s.length(); i++) {
            String tempString = longestPalindromeHelper(s, i, i);
            longestString = longestString.length() > tempString.length() ? longestString : tempString;
            tempString = longestPalindromeHelper(s, i, i + 1);
            longestString = longestString.length() > tempString.length() ? longestString : tempString;
        }
        return longestString;
    }
    private String longestPalindromeHelper(String str, int start, int end) {
        while (start >= 0 && end < str.length() && str.charAt(start) == str.charAt(end)) {
            start--;
            end++;
        }
        return str.substring(start + 1, end--);
    }
    /**
     * O(n^3) solution but not accepted
     * @param s
     * @return
     */
    public String longestPalindromeI(String s) {
        if (s == null || s.length() <= 1) {
            return s;
        }
        Map<String, Boolean> evaluatedStringMap = new HashMap<>();
        String longestString = "";
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j <= s.length(); j++) {
                String subString = s.substring(i, j);
                if (isPalindrome(subString, evaluatedStringMap) && subString.length() > longestString.length()) {
                    longestString = subString;
                }
            }
        }
        return longestString;
    }
    private boolean isPalindrome(String s, Map<String, Boolean> evaluatedStringMap) {
        if (s.length() == 0) {
            return true;
        } else if (evaluatedStringMap.containsKey(s)) {
            return evaluatedStringMap.get(s);
        }
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l) != s.charAt(r)) {
                return false;
            }
            l++;
            r--;
        }
        evaluatedStringMap.put(s, true);
        return true;
    }

    /**
     * O(n^2) solution but accepted by leetcode
     * @param s
     * @return
     */
    public String longestPalindromeII(String s) {
        if(s == null || s.length() <= 1) {
            return s;
        }
        int len = s.length();
        boolean[][] dp = new boolean[len][len];
        String longestStr = "";
        int maxLen = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            for (int j = i; j < s.length(); j++) {
                if (s.charAt(i) == s.charAt(j) && (j - i <= 2 || dp[i + 1][j - 1])) {
                    dp[i][j] = true;
                    if (maxLen < j - i + 1) {
                        longestStr = s.substring(i, j + 1);
                        maxLen = j - i + 1;
                    }
                }
            }
        }
        return longestStr;
    }

    public static void main(String[] args) {
        LongestPalindrome longestPalindrome = new LongestPalindrome();
        System.out.println(longestPalindrome.longestPalindromeII("zudfweormatjycujjirzjpyrmaxurectxrtqedmmgergwdvjmjtstdhcihacqnothgttgqfywcpgnuvwglvfiuxteopoyizgehkwuvvkqxbnufkcbodlhdmbqyghkojrgokpwdhtdrwmvdegwycecrgjvuexlguayzcammupgeskrvpthrmwqaqsdcgycdupykppiyhwzwcplivjnnvwhqkkxildtyjltklcokcrgqnnwzzeuqioyahqpuskkpbxhvzvqyhlegmoviogzwuiqahiouhnecjwysmtarjjdjqdrkljawzasriouuiqkcwwqsxifbndjmyprdozhwaoibpqrthpcjphgsfbeqrqqoqiqqdicvybzxhklehzzapbvcyleljawowluqgxxwlrymzojshlwkmzwpixgfjljkmwdtjeabgyrpbqyyykmoaqdambpkyyvukalbrzoyoufjqeftniddsfqnilxlplselqatdgjziphvrbokofvuerpsvqmzakbyzxtxvyanvjpfyvyiivqusfrsufjanmfibgrkwtiuoykiavpbqeyfsuteuxxjiyxvlvgmehycdvxdorpepmsinvmyzeqeiikajopqedyopirmhymozernxzaueljjrhcsofwyddkpnvcvzixdjknikyhzmstvbducjcoyoeoaqruuewclzqqqxzpgykrkygxnmlsrjudoaejxkipkgmcoqtxhelvsizgdwdyjwuumazxfstoaxeqqxoqezakdqjwpkrbldpcbbxexquqrznavcrprnydufsidakvrpuzgfisdxreldbqfizngtrilnbqboxwmwienlkmmiuifrvytukcqcpeqdwwucymgvyrektsnfijdcdoawbcwkkjkqwzffnuqituihjaklvthulmcjrhqcyzvekzqlxgddjoir"));
    }
}
