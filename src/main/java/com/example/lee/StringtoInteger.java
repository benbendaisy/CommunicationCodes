package com.example.lee;

/**
 * Created by benbendaisy on 3/3/15.
 *
 * Implement atoi to convert a string to an integer.
 *
 * Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
 *
 * Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
 *
 * Update (2015-02-10):
 * The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button  to reset your code definition.
 *
 *
 */
public class StringtoInteger {
    public int atoi(String str) {
        if (null == str || str.length() == 0) {
            return 0;
        }

        str = str.trim();
        //handle all white spaces case
        if (str.length() == 0) {
            return 0;
        }

        boolean isNegative = false;
        if ('-' == str.charAt(0)) {
            isNegative = true;
            str = str.substring(1);
        } else if ('+' == str.charAt(0)) {
            str = str.substring(1);
        }

        double res = 0;
        int idx = 0;
        while (idx < str.length()) {
            if (str.charAt(idx) >= '0' && str.charAt(idx) <= '9') {
                res = res * 10 + (str.charAt(idx) - '0');
            } else {
                break;
            }
            idx++;
        }

        if (isNegative) {
            res = -res;
            return res < Integer.MIN_VALUE ? Integer.MIN_VALUE : (int) res;
        } else {
            return res > Integer.MAX_VALUE ? Integer.MAX_VALUE : (int) res;
        }
    }
}
