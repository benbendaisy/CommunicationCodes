package com.example.digits;

/**
 * Created by benbendaisy on 3/11/15.
 */
public class Count4InNumber {
    private boolean contains4(int num) {
        while (num >= 4) {
            if (num % 10 == 4) {
                return true;
            }
            num /= 10;
        }
        return false;
    }

    public int Count4s(int num) {
        int count = 0;
        for (int i = 4; i < num; i++) {
            if (contains4(i)) {
                count++;
            }
        }
        return count;
    }
}
