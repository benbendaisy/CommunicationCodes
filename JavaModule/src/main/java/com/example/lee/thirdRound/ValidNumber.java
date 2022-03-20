package com.example.lee.thirdRound;

/**
 * Created by benbendaisy on 7/12/17.
 */
public class ValidNumber {
    public boolean isNumber(String s) {
        if (s == null) {
            return false;
        }

        String str = s.trim();
        if (str.length() == 0) {
            return false;
        }
        int idx = 0;
        if (str.charAt(idx) == '-' || str.charAt(idx) == '+') {
            str = str.substring(1);
        }

        if (str.startsWith(".e") || str.startsWith("e.")) {
            return false;
        }

        boolean hasE = false, hasDot = false;
        while (idx < str.length()) {
            char ch = str.charAt(idx);
            if (ch == 'e') {
                if (idx == 0 || idx == str.length() - 1 || hasE) {
                    return false;
                }
                hasE = true;
            } else if (ch == '.') {
                if (hasE || hasDot || str.length() == 1) {
                    return false;
                } else if (idx == str.length() - 1) {
                    if (idx > 0 && (str.charAt(idx - 1) == 'e' || str.charAt(idx - 1) == '+' || str.charAt(idx - 1) == '-')) {
                        return false;
                    }
                }
                hasDot = true;
            } else if (ch == '-' || ch == '+') {
                if (!hasE || str.charAt(idx - 1) != 'e' || idx == str.length() - 1) {
                    return false;
                }
            } else if (ch < '0' || ch > '9') {
                return false;
            }
            idx++;
        }
        return true;
    }

    public static void main(String[] args) {
        ValidNumber validNumber = new ValidNumber();
        System.out.println(validNumber.isNumber("0"));
        System.out.println(validNumber.isNumber(" 0.1 "));
        System.out.println(validNumber.isNumber("abc"));
        System.out.println(validNumber.isNumber("1 a"));
        System.out.println(validNumber.isNumber("2e10"));
        System.out.println(validNumber.isNumber("0.1"));
        System.out.println(validNumber.isNumber("+.1"));
        System.out.println(validNumber.isNumber("+."));
        System.out.println(validNumber.isNumber("+E3"));
        System.out.println(validNumber.isNumber("46.e3"));
        System.out.println(validNumber.isNumber("46.e+3"));
        System.out.println(validNumber.isNumber("46.e-3"));
        System.out.println(validNumber.isNumber("46.e3.0"));
    }

}
