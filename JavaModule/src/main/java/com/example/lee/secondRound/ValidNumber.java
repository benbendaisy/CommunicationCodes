package com.example.lee.secondRound;

/**
 * Created by benbendaisy on 5/16/15.
 */
public class ValidNumber {
    public boolean isNumber(String s) {
        if (null == s || s.length() == 0) return false;
        boolean isN = false;
        s = s.trim();
        int idx = 0;
        //handle the cases: 1, "  "; 2, "e" or "."; 3, ends with "e", "+" or "-"
        if (s.length() == 0 || (s.length() == 1 && (s.charAt(0) == 'e' || s.charAt(0) == '.')) || s.startsWith("e") || s.endsWith("e") || s.endsWith("+") || s.endsWith("-")) return false;
        char ch = s.charAt(idx);
        if (ch == '+' || ch == '-') {
            idx++;
            //handle the cases: 1, +/- followed by e; 2, "+." or "-."
            if ((idx == s.length() - 1 && s.charAt(idx) == '.') || s.charAt(idx) == 'e') return false;
        }
        int pCnt = 0;
        boolean hasE = false;
        while (idx < s.length()) {
            ch = s.charAt(idx);
            if (isNum(ch)) {
                idx++;
                continue;
            }
            switch(ch) {
                //handle the cases: 1, more than one "."; 2, "." followed by "e"; 3, "e" is before "."
                case '.': pCnt++; if (pCnt > 1 || (idx == 0 && s.charAt(idx + 1) == 'e') || hasE) return false; break;
                case '+':
                //handle the cases: 1, more than two "+" or "-" without "e"; 2, "+" and "-" are not followed by "e"
                //"." followed by "+" or "-" without "e"
                case '-': if (!hasE || (idx > 0 && (s.charAt(idx - 1) != 'e' || s.charAt(idx - 1) == '.'))) return false; break;
                //has more than one "e"
                case 'e': if (hasE) return false; hasE = true; break;
                default: return false;
            }
            idx++;
        }
        return true;
    }

    private boolean isNum(char ch) {
        return ch >= '0' && ch <= '9';
    }
}
