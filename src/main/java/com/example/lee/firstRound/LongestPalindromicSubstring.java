package com.example.lee.firstRound;

/**
 * Created by benbendaisy on 3/3/15.
 *
 * Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.
 */
public class LongestPalindromicSubstring {

    //o(n^2) solution
    public String longestPalindrome(String s) {
        if (null == s || s.length() < 2) {
            return s;
        }
        String maxStr = "";
        for (int i = 0; i < s.length() -1; i++) {
            String str = expandStr(s, i, i);
            if (maxStr.length() < str.length()) {
                maxStr = str;
            }

            if (s.charAt(i) == s.charAt(i + 1)) {
                str = expandStr(s, i, i+1);
                if (maxStr.length() < str.length()) {
                    maxStr = str;
                }
            }
        }
        return maxStr;
    }

    private String expandStr(String str, int l, int r) {
        while (l >= 0 && r < str.length() && str.charAt(l) == str.charAt(r)) {
            l--;
            r++;
        }
        return str.substring(l + 1, r);
    }

    //o(n^3) solution
    public String longestPalindromeI(String s) {
        if (null == s || s.length() < 2) {
            return s;
        }

        String maxStr = "";
        for (int i = 0; i < s.length(); i++) {
            for (int j = i + 1; j <= s.length(); j++) {
                String str = s.substring(i, j);

                if (str.length() > maxStr.length() && isPalindrome(str)) {
                    maxStr = str;
                }
            }
        }

        return maxStr;
    }

    private boolean isPalindrome(String str) {
        int left = 0, right = str.length() - 1;
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }

    //o(n) solution, refer to http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
    //http://www.felix021.com/blog/read.php?2040
    public String longestPalindromeII(String s) {
        if (null == s || s.length() < 2) {
            return s;
        }

        //pre handling string
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < s.length(); i++) {
            sb.append("#");
            sb.append(s.charAt(i));
        }
        sb.append("#");
        String str = sb.toString();
        int[] p = new int[str.length()];
        int r = 0, c = 0;
        int maxLen = 0, idx = 0;
        //calculating p
        for (int i = 0; i < str.length(); i++) {
            int l = 2 * c - i;
            p[i] = r > i && l > 0 ? Math.min(p[l], r - i) : 1;

            while (i + p[i] < str.length() && i - p[i] >= 0 && str.charAt(i + p[i]) == str.charAt(i - p[i])) {
                p[i]++;
            }

            if (i + p[i] > r) {
                r = i + p[i];
                c = i;
                //save max string and center
                if (maxLen < p[i]) {
                    maxLen = p[i];
                    idx = i;
                }
            }
        }

        //handle return string
        if (maxLen > 0) {
            return s.substring((idx - maxLen + 1)/2, (idx + maxLen)/2);
        } else {
            return "";
        }
    }

    public static void main(String[] args) {
        LongestPalindromicSubstring longestPalindromicSubstring = new LongestPalindromicSubstring();

        //System.out.println(longestPalindromicSubstring.expandStr("abcd", 0, 1));
        System.out.println(longestPalindromicSubstring.longestPalindrome("nmngaowrbsssvihklwmuqshcddwlxrywrlwtennwfvrevgvhsvgeccfulmuvrcksdmgeqrblnlwoepefhcwhmgyvgcoyyygrmttyfycxwbqktpurlcfhzlakhmrddsydgygganpmaglaxyhfwjusukzcnakznygqplngnkhcowavxoiwrfycxwdkxqfcjqwyqutcpyedbnuogedwobsktgioqdczxhikjrbkmqspnxcpngfdwdaboscqbkwforihzqdcppxjksiujfvlpdjryewaxgmdgigvxdlstxwngtbdrrkfudjinzyxbdmkautclvvyguekuzwwetmsxittgtxbnvvrgasvnlogdiepltweaehubwelznidltzlbzdsrxmhjpkmylnwkdsxnpkplkdzywioluaqguowtbaoqzqgjfewphqcvlnwlojbxgomvxxkhwwykawegxubjiobizicuxzeafgautefsurgjlbhcfevqzsbhwxycrcaibdsgluczcuewzqupakbzmcvzsfodbmgtugnihyhqkvyeboqhqldifbxuaxqzxtyejoswikbzpsvzkxcndgeyvfnyrfbkhlalzpqjueibnodamgpnxlkvwvliouvejcpnakllfxepldfmdzszagkyhdgqqbkb"));
        System.out.println(longestPalindromicSubstring.longestPalindromeI("nmngaowrbsssvihklwmuqshcddwlxrywrlwtennwfvrevgvhsvgeccfulmuvrcksdmgeqrblnlwoepefhcwhmgyvgcoyyygrmttyfycxwbqktpurlcfhzlakhmrddsydgygganpmaglaxyhfwjusukzcnakznygqplngnkhcowavxoiwrfycxwdkxqfcjqwyqutcpyedbnuogedwobsktgioqdczxhikjrbkmqspnxcpngfdwdaboscqbkwforihzqdcppxjksiujfvlpdjryewaxgmdgigvxdlstxwngtbdrrkfudjinzyxbdmkautclvvyguekuzwwetmsxittgtxbnvvrgasvnlogdiepltweaehubwelznidltzlbzdsrxmhjpkmylnwkdsxnpkplkdzywioluaqguowtbaoqzqgjfewphqcvlnwlojbxgomvxxkhwwykawegxubjiobizicuxzeafgautefsurgjlbhcfevqzsbhwxycrcaibdsgluczcuewzqupakbzmcvzsfodbmgtugnihyhqkvyeboqhqldifbxuaxqzxtyejoswikbzpsvzkxcndgeyvfnyrfbkhlalzpqjueibnodamgpnxlkvwvliouvejcpnakllfxepldfmdzszagkyhdgqqbkb"));
        System.out.println(longestPalindromicSubstring.longestPalindromeII("nmngaowrbsssvihklwmuqshcddwlxrywrlwtennwfvrevgvhsvgeccfulmuvrcksdmgeqrblnlwoepefhcwhmgyvgcoyyygrmttyfycxwbqktpurlcfhzlakhmrddsydgygganpmaglaxyhfwjusukzcnakznygqplngnkhcowavxoiwrfycxwdkxqfcjqwyqutcpyedbnuogedwobsktgioqdczxhikjrbkmqspnxcpngfdwdaboscqbkwforihzqdcppxjksiujfvlpdjryewaxgmdgigvxdlstxwngtbdrrkfudjinzyxbdmkautclvvyguekuzwwetmsxittgtxbnvvrgasvnlogdiepltweaehubwelznidltzlbzdsrxmhjpkmylnwkdsxnpkplkdzywioluaqguowtbaoqzqgjfewphqcvlnwlojbxgomvxxkhwwykawegxubjiobizicuxzeafgautefsurgjlbhcfevqzsbhwxycrcaibdsgluczcuewzqupakbzmcvzsfodbmgtugnihyhqkvyeboqhqldifbxuaxqzxtyejoswikbzpsvzkxcndgeyvfnyrfbkhlalzpqjueibnodamgpnxlkvwvliouvejcpnakllfxepldfmdzszagkyhdgqqbkb"));
    }
}
