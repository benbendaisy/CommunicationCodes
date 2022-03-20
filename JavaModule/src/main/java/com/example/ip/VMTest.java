package com.example.ip;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

/**
 * Created by pzhong1 on 4/25/15.
 */
public class VMTest {
    private static void printFailMessage(int idx) {
        String message = String.format("FAILURE => WRONG INPUT (LINE %d)", idx);
        System.out.println(message);
    }

    private static void printFailMessage(int idx1, int idx2) {
        String message = String.format("FAILURE => RECEIVED: %d, EXPECTED: %d", idx1, idx2);
        System.out.println(message);
    }

    private static void printSuccessMessage(int idx1) {
        String message = String.format("SUCCESS => RECEIVED: %d", idx1);
        System.out.println(message);
    }

    public static boolean isValidInteger(String str) {
        try {
            Integer.parseInt(str);
        } catch (NumberFormatException e) {
            //not a valid integer
            return false;
        }
        return true;
    }

    private static boolean isValidInteger(String[] strs) {
        Set<String> set = new HashSet<String>();
        for (String str : strs) {
            if (!set.add(str) || !isValidInteger(str)) return false;
        }
        return true;
    }

    private static int getMax(String[] strs) {
        int max = Integer.MIN_VALUE;
        for (String str : strs) {
            max = Math.max(max, Integer.parseInt(str));
        }
        return max;
    }

    private static int getMin(String[] strs) {
        int min = Integer.MAX_VALUE;
        for (String str : strs) {
            min = Math.min(min, Integer.parseInt(str));
        }
        return min;
    }

    public static void main(String args[] ) throws Exception {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        if (null == input || !isValidInteger(input)) {
            printFailMessage(1);
            return;
        }
        int n = Integer.parseInt(input);
        int count = 0;
        while ((input = br.readLine()) != null) {
            count++;
            if (count > n + 1) {
                printFailMessage(count);
            } else {
                if (input.length() == 0) {
                    printFailMessage(count);
                    continue;
                }
                String[] tasks = input.split(" ", -1);
                if (!isValidInteger(tasks)) {
                    printFailMessage(count);
                    continue;
                }

                int max = getMax(tasks);
                if (max != tasks.length) {
                    printFailMessage(tasks.length, max);
                } else {
                    int min = getMin(tasks);
                    if (min != 1) {
                        printFailMessage(count);
                        continue;
                    }
                    printSuccessMessage(max);
                }
            }
        }
    }
}
